# 🧠 AI Chatbot using LangChain, Ollama (LLaMA 3.2:1b), Langfuse & Streamlit

This is an interactive AI chatbot built with **LangChain**, **Ollama**, and **Langfuse**, wrapped in a sleek **Streamlit** UI. It utilizes the lightweight **LLaMA 3.2:1b** model for local inference and supports conversational memory via LangChain.

---

## 💡 Features

- 🔁 **Conversational Memory** using LangChain’s `ConversationBufferMemory`
- 🤖 **LLM-powered Chat** using the Ollama runtime with `llama3.2:1b`
- 📊 **Observability** with Langfuse integration for trace and logs
- 💬 **Streamlit Interface** with styled chat UI
- 🔐 **.env Integration** for secure Langfuse keys

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Madhurithotakua/llama3-chatbot-langchain-langfuse.git
cd llama3-chatbot-langchain-langfuse
```

### 2. Create a virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your `.env` file

Create a `.env` file in the root directory with your Langfuse credentials:

```
LANGFUSE_PUBLIC_KEY=your_public_key
LANGFUSE_SECRET_KEY=your_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
```

### 5. Make sure Ollama is running with the LLaMA model

Install Ollama and pull the model:

```bash
ollama run llama3.2:1b
```

---

## 🧪 Run the Chatbot

```bash
streamlit run app.py
```

---

## 📸 Preview

(Add your screenshot here)

---

## 🛠 Tech Stack

- LangChain  
- Ollama  
- Langfuse  
- Streamlit  
- Python  

---

## 🧠 What is Langfuse?

**Langfuse** is a powerful observability platform designed for LLM apps. It lets you log, trace, and monitor LLM chains and interactions, helping you debug and optimize your AI workflows.

---

## 🗃️ File Structure

```
├── app.py               # Main Streamlit chatbot app
├── .env                 # Secret keys and config
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🙌 Credits

Built by **Madhuri Thotakura**  
Inspired by modern LLM stack tooling!

---

## 📄 License

This project is licensed under the **MIT License**.
