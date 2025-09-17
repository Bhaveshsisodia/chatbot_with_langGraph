# 🤖 Chatbot with LangGraph

An interactive AI-powered chatbot built with **LangGraph** and **Streamlit**.  
This project demonstrates how to design, stream, and style conversational AI messages with persistent session history, making the chatbot feel natural and user-friendly.

---

## 🚀 Features
- ⚡ **LangGraph-powered reasoning** — structured agent workflow for handling conversations  
- 💬 **Streaming responses** — assistant messages appear in real-time  
- 🎨 **Custom chat UI** — styled user and assistant bubbles (WhatsApp/ChatGPT-like)  
- 📜 **Conversation history** — persists across turns using Streamlit’s session state  
- 🔌 **Easy integration** — plug in any LLM backend via LangChain/LangGraph  

---

## 🛠️ Tech Stack
- [LangGraph](https://www.langchain.com/langgraph) – agent orchestration  
- [LangChain](https://www.langchain.com/) – LLM framework  
- [Streamlit](https://streamlit.io/) – frontend for chat interface  
- **Python**

---

## 📸 Demo
> *(Add a screenshot or GIF of your chatbot UI here)*

---
## 📂 Project Structure
.
├── chatbot_backend.py # LangGraph workflow & tools
├── app.py # Streamlit frontend
├── requirements.txt # Dependencies
└── README.md # Project docs


---

## 🚦 Getting Started

```bash
# Clone the repository
git clone https://github.com/your-username/langgraph-chatbot.git
cd langgraph-chatbot

# Install dependencies
pip install -r requirements.txt

# Run the chatbot
streamlit run app.py

## 📂 Project Structure
