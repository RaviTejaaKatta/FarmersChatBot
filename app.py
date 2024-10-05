import streamlit as st
from model_tokeniser import model, tokenizer
from streamlit_chat import message

from generate_responses import generate_response
from TextToSpeech import text_to_speech
from AudioToText import Speech_to_text

if 'history' not in st.session_state:
    st.session_state['history'] = []

# User input section
user_input = st.text_input("You: ", key="input")

if user_input:
    # Add user input to chat history
    st.session_state['history'].append({"message": user_input, "is_user": True})

    # Generate bot response
    bot_response = generate_response(user_input, model, tokenizer)
    try:
        if st.button("🎧", key="audio_button"):
            st.audio(text_to_speech(bot_response))
    except Exception as e:
        st.write(f"error occured {e}")
    st.session_state['history'].append({"message": bot_response, "is_user": False})


# Display the chat history
for i, chat in enumerate(st.session_state['history']):
    message(chat['message'], is_user=chat['is_user'], key=f"message_{i}")
    