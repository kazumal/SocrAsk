import streamlit as st
import openai
import os
from dotenv import load_dotenv

def load_css(file):
    with open(file, "r") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# load_css("styles/Chat.css")

# Set up API key and contact email
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Streamlit header
st.markdown("<div class='container'><div class='title'><h1>SocrAsk Chat</h1></div>", unsafe_allow_html=True)
st.markdown("<div class='history'>", unsafe_allow_html=True)

# Initialize session_state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are an assistant that provides helpful information, suggests topics for deeper understanding, avoids asking too many questions, praises the user, and occasionally shares witty jokes."},
    ]

def display_conversation_history():
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.write(f"User: {message['content']}")
        elif message["role"] == "assistant":
            st.write(f"Assistant: {message['content']}")

display_conversation_history()

# Footer with text input and buttons
st.markdown("</div><div class='footer'>", unsafe_allow_html=True)
user_input = st.text_input("", key="user_input", css_classes=["user-input"])

# Submit button as icon
if st.button("", key="submit_button", css_classes=["submit-button"], icon="send"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages,
    )
    assistant_response = response.choices[0].message['content']
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    display_conversation_history()

# Test and reset buttons as icons
if st.button("", key="test_button", css_classes=["submit-button"], icon="question"):
    user_input = "test"
    st.session_state.messages.append({"role": "user", "content": "Please generate 3 multiple-choice questions with 4 answer options each to test my understanding about we talked."})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages,
    )
    assistant_response = response.choices[0].message['content']
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    display_conversation_history()

if st.button("", key="reset_button", css_classes=["submit-button"], icon="redo"):
    st.session_state.messages = [
        {"role": "system", "content": "You are a tutor who always responds in Socratic style..."},
        {"role": "system", "content": "Always end the sentence with a specific example question..."},
    ]
    display_conversation_history()

st.markdown("</div></div>", unsafe_allow_html=True)
