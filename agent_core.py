import asyncio
import os
from semantic_kernel import Kernel
from semantic_kernel.contents import ChatHistory
from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import (
    OpenAIChatCompletion,
    OpenAIChatPromptExecutionSettings,
)
from plugins.database_plugin import DatabasePlugin
from plugins.github_plugin import GitHubPlugin
from plugins.logger_plugin import LoggerPlugin


async def _run_agent_async(message: str, chat: ChatHistory = None) -> str:
    kernel = Kernel()

    chat_service = OpenAIChatCompletion(
        ai_model_id="gpt-4.1",
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    kernel.add_service(chat_service)
    kernel.add_plugin(DatabasePlugin(), "DatabasePlugin")
    kernel.add_plugin(GitHubPlugin(), "GitHubPlugin")
    kernel.add_plugin(LoggerPlugin(), "LoggerPlugin")

    settings = OpenAIChatPromptExecutionSettings()
    settings.function_choice_behavior = FunctionChoiceBehavior.Auto()
    settings.temperature = 0.6

    # create history of the chat if not provided
    if chat is None:
        chat = ChatHistory()
        chat.add_system_message(
            "You are an assistant that can query and modify the 'sales' database, "
            "manage GitHub issues, and return logs on request. "
            "Respond clearly using Markdown formatting."
        )

    # add user message to chat history
    chat.add_user_message(message)

    # get response from the agent
    response = await chat_service.get_chat_message_content(
        chat_history=chat,
        settings=settings,
        kernel=kernel,
    )
    return str(response)


def run_agent(message: str, chat: ChatHistory = None) -> str:
    """ Run the agent synchronously. """
    try:
        return asyncio.run(_run_agent_async(message, chat))
    except RuntimeError:
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(_run_agent_async(message, chat))
