import streamlit as st
from pathlib import Path

image_dir = Path("./images")
human_icon = image_dir / "human_icon.png"
ai_icon = image_dir / "ai_icon.png"
icons = {"user": human_icon, "assistant": ai_icon}

if st.session_state.get("history") is None:
    st.session_state.history = []

first_speaker = st.radio("最初の発話者", ["User", "Assistant"])
clear_button = st.button("Clear")
if clear_button:
    st.session_state.history = []
prompt = st.chat_input("ここにメッセージを入力")
if prompt:
    st.session_state.history.append(prompt)
    if first_speaker == "User":
        speakers = ["user", "assistant"]
    else:
        speakers = ["assistant", "user"]

    for i, message in enumerate(st.session_state.history):
        s = speakers[i % 2]
        with st.chat_message(s, avatar=str(icons[s])):
            st.markdown(message)
