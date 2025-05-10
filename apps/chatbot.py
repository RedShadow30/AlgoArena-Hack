import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="wide")

import rag.rag as rag

def app():
    left_col, center_col, right_col = st.columns([1, 2, 1])

    with center_col:
        st.title("Chatbot Page")
        
        with st.chat_message("assistant"):
            st.write("Hey there! What questions do you have about food sustainability?")
        
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        add_vertical_space(3)

        # Assign user input to prompt var
        if prompt := st.chat_input("Type your question here..."):
            # Display user msg in chat
            with st.chat_message("user"):
                st.markdown(prompt)

            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Get response from the chatbot
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = rag.get_answer(prompt)
                    st.markdown(response)

            # Add assistant message to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})