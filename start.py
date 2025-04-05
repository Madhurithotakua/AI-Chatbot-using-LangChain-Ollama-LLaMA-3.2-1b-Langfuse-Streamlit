import os
import streamlit as st
import ollama
from dotenv import load_dotenv
from langfuse import Langfuse
from langchain.memory import ConversationBufferMemory
from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Initialize Langfuse for logging
langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST"),
)

# Streamlit page config
st.set_page_config(page_title="AI Chatbot", layout="centered")

import streamlit as st

st.markdown("""
    <style>
        .main {
            display: flex;
            justify-content: center;
        }
        .chat-container {
            max-width: 600px;
            padding: 10px;
            border-radius: 10px;
        }
        .chat-heading {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .user-message {
            background-color: #f1f1f1;
            padding: 10px;
            border-radius: 10px;
            max-width: 70%;
            margin-left: auto;
            text-align: right;
            display: flex;
            align-items: center;
            justify-content: flex-end;
            gap: 8px;
        }
        .bot-message {
            padding: 10px;
            border-radius: 10px;
            width: fit-content;
            max-width: 80%;
            text-align: left;
            word-wrap: break-word;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .user-icon, .bot-icon {
            font-size: 20px;
            font-weight: bold;
        }

        /* Styling for input box */
        .stChatInput textarea {
            background-color: #333 !important;  /* Dark background */
            color: white !important;  /* White text */
            border: 2px solid #555 !important;  /* Darker border */
            border-radius: 5px !important;
            caret-color: white !important; /* White cursor */
        }

        /* Styling for send button */
        .stChatInput button {
            color: white !important;
            border-radius: 5px !important;
        }

        /* Adding a static header */
        .static-header {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 20px;
            color: #ffffff;
            background-color: #333;
            padding: 15px;
            border-radius: 10px;
        }

    </style>
""", unsafe_allow_html=True)

# Static header
st.markdown('<div class="static-header">Llama3.2:1b Chatbot</div>', unsafe_allow_html=True)


# Display heading
st.markdown('<div class="chat-heading">🤖 AI Chatbot using LangChain, Langfuse & Ollama</div>', unsafe_allow_html=True)

# Initialize conversation memory
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True
    )

# Define LangChain LLM
llm = Ollama(model="llama3.2:1b")  # Ensure Ollama is running

# Define the conversation prompt template
prompt = PromptTemplate(
    input_variables=["chat_history", "user_message"],
    template="""You are an intelligent chatbot. Continue the conversation naturally.
    Chat history: {chat_history}
    User: {user_message}
    Bot:"""
)

# Create LLMChain with memory
llm_chain = LLMChain(llm=llm, prompt=prompt, memory=st.session_state.memory)

# Chat message container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history with icons
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'''
            <div class="user-message">
                <span>{msg["content"]}</span>
                <span class="user-icon">👤</span>
            </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown(f'''
            <div class="bot-message">
                <span class="bot-icon">🤖</span>
                <span>{msg["content"]}</span>
            </div>
        ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# User input field
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user input to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate response with LangChain
    bot_reply = llm_chain.run(user_message=user_input)

    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Display messages with styling
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown(f'''
        <div class="user-message">
            <span>{user_input}</span>
            <span class="user-icon">👤</span>
        </div>
    ''', unsafe_allow_html=True)
    st.markdown(f'''
        <div class="bot-message">
            <span class="bot-icon">🤖</span>
            <span>{bot_reply}</span>
        </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Log the interaction using Langfuse
    trace = langfuse.trace(
        name="chatbot_interaction",
        user_id="test_user",
        input={"user_message": user_input},
        output={"bot_reply": bot_reply}
    )

    # Ensure the trace is sent to Langfuse
    langfuse.shutdown()
