import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from agent.orchestrator import ask

st.set_page_config(
    page_title="Enterprise AI Knowledge Bot",
    page_icon="🤖",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

#############################################
# Sidebar
#############################################

with st.sidebar:

    st.title("🤖 Enterprise AI Knowledge Bot")

    st.success("System Online")

    st.divider()

    st.subheader("🧰 AI Tools")

    st.success("📚 RAG Knowledge Search")

    st.success("🗄 PostgreSQL (Supabase)")

    st.success("📧 Gmail Search")

    st.success("🌦 Weather")

    st.success("🧮 Calculator")

    st.divider()

    st.subheader("💾 Memory")

    st.info("Long-Term Memory (Qdrant)")

    st.success("Enabled")

    st.divider()

    st.subheader("🧠 AI Agent")

    st.write("OpenAI Tool Calling")

    st.write("Reasoning Enabled")

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.messages=[]

        st.rerun()

#############################################
# Main
#############################################

st.title("🤖 Enterprise AI Knowledge Bot")

st.caption(
    "RAG + Tool Calling + Persistent Memory + AI Agent"
)

#############################################
# Display Previous Messages
#############################################

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

#############################################
# Chat Input
#############################################

prompt = st.chat_input(
    "Ask anything..."
)

if prompt:

    st.session_state.messages.append({

        "role":"user",

        "content":prompt

    })

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = ask(prompt)

            st.markdown(answer)

    st.session_state.messages.append({

        "role":"assistant",

        "content":answer

    })