import streamlit as st
from semantic_kernel.contents import ChatHistory
from agent_core import run_agent


# Page setup
st.set_page_config(page_title="AI Assistant Chat", page_icon="🤖", layout="wide")

st.title("🤖 AI Assistant Chat")


# About the assistant
with st.expander("ℹ️ What this assistant can do", expanded=True):
    st.markdown("""
    This **smart assistant** uses **Semantic Kernel** and **OpenAI GPT-4.1**  
    to help you work with your data and tools.

    It can:
    - 🧾 **Manage GitHub issues** – create, edit, or close issues  
    - 🗄 **Work with the 'sales' database** – run SQL queries, view data, and see the schema  
    - 🪵 **Read system logs** – show recent log entries on request  
    - 💬 **Answer questions in natural language** – using context and Markdown formatting  

    > 💡 Just type what you need, for example:  
    > “Show the last 5 orders”,  
    > “Create a GitHub issue about slow API”,  
    > or “Show logs from the last 10 minutes”.
    """)

st.divider()


# Chat initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatHistory()
    st.session_state.messages = []
    st.session_state.chat_history.add_system_message(
        "You are an assistant that can query and modify the 'sales' database, "
        "manage GitHub issues, and return logs on request. "
        "Respond clearly and use Markdown formatting."
    )


# Chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# Input box
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run_agent(prompt, st.session_state.chat_history)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.session_state.chat_history.add_assistant_message(response)

    st.rerun()

# Clear chat button
if st.button("🧹 Clear chat"):
    st.session_state.messages = []
    st.session_state.chat_history = ChatHistory()
    st.session_state.chat_history.add_system_message(
        "You are an assistant that can query and modify the 'sales' database, "
        "manage GitHub issues, and return logs on request. "
        "Respond clearly and use Markdown formatting."
    )
    st.success("Chat cleared ✅")
