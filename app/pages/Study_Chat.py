import codecs
import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Set up API key and contact email
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Streamlit header and body
st.header("SocrAsk Chat")
user_input = st.text_input("Enter your question:")
submit_button = st.button("Submit")
test_button = st.button("Test")
reset_button = st.button("Reset")
st.write("Conversation History:")

# Initialize session_state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are an assistant that provides helpful information."},
    ]

def display_conversation_history():
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.write(f"User: {message['content']}")
        elif message["role"] == "assistant":
            st.write(f"Assistant: {message['content']}")

button_pressed = False

if reset_button:
    st.session_state.messages = [
        {"role": "system", "content": "You are an assistant that provides helpful information, suggests topics for deeper understanding."},
    ]
    display_conversation_history()
    button_pressed = True

if submit_button:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages,
    )
    assistant_response = response.choices[0].message['content']
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    display_conversation_history()
    button_pressed = True

if test_button:
    user_input = "test"
    st.session_state.messages.append({"role": "user", "content": "Please generate 3 multiple-choice questions with 4 answer options each to test my understanding about we talked."})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages,
    )
    assistant_response = response.choices[0].message['content']
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    display_conversation_history()
    button_pressed = True

if not button_pressed:
    display_conversation_history()

st.write(st.session_state.messages)