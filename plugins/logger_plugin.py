from semantic_kernel.functions import kernel_function, KernelArguments
from .agent_logger import AgentLogger


class LoggerPlugin:
    @kernel_function(
        name="GetLogs",
        description="Return system logs for the last N minutes. Example: 'GetLogs 15' will show logs for 15 minutes.'"
    )
    async def get_logs(self, minutes: int = 10, arguments: KernelArguments = None) -> str:
        """Return logs only when the user explicitly asks."""
        return AgentLogger.read_logs_for_period(minutes)
