import streamlit as st
from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage




st.set_page_config(page_title="Chatbot", page_icon="✨")

st.markdown(
    """
    <h1 style="
        text-align: center;
        font-size: 50px;
        background: -webkit-linear-gradient(#00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    ">
        🤖 Chatbot
    </h1>
    """,
    unsafe_allow_html=True
)

def message(text, is_user=False):
    if is_user:
        st.markdown(
            f"""
            <div style='
                background-color: #DCF8C6;
                padding: 12px;
                border-radius: 15px;
                margin: 8px 0px;
                text-align: right;
                font-size: 16px;
                max-width: 70%;
                margin-left: auto;'>
                👤 {text}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style='
                background-color: #E8EAF6;
                padding: 12px;
                border-radius: 15px;
                margin: 8px 0px;
                text-align: left;
                font-size: 16px;
                max-width: 70%;
                margin-right: auto;'>
                🤖 {text}
            </div>
            """,
            unsafe_allow_html=True
        )



CONFIG = {'configurable':{'thread_id':"thread-1"}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] =[]

# for loading conversation

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

#{'role':'user' , 'content':"Hi"}
# {'role':'assistant', 'content':'Hello'}

user_input = st.chat_input('Type Here')

if user_input:

    # Save user message
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})

    # Show user message
    with st.chat_message("user"):
        st.markdown(f"<div style='background-color:#DCF8C6; color:black; padding:10px; border-radius:10px; display:inline-block;'>"
                f"👤 {user_input}</div>", unsafe_allow_html=True)
    # Get AI response
    response = chatbot.invoke(
        {'messages': [HumanMessage(content=user_input)]},
        config=CONFIG
    )
    ai_message = response['messages'][-1].content

    # Save assistant message
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})

    # Show assistant message
    with st.chat_message("assistant"):
        st.markdown(f"<div style='background-color:#E8EAF6; color:black; padding:10px; border-radius:10px; display:inline-block;'>"
                f"🤖 {ai_message}</div>", unsafe_allow_html=True)   # instead of message(...)
