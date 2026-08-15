
import streamlit as st
from chatbot import get_response


st.set_page_config(
    page_title="AI Student Support Chatbot",
    page_icon="🎓",
    layout="wide"
)


# ---------- PAGE HEADER ----------

st.title("🎓 AI Student Support Chatbot")

st.write(
    "Welcome! I can help you with admissions, fees, examinations, "
    "library, hostel, scholarships, placements and other student support services."
)


# ---------- SIDEBAR ----------

with st.sidebar:
    st.header("🎓 Student Services")

    st.write("You can ask about:")

    st.markdown("""
    🏫 **Admissions**

    💰 **Fees**

    📝 **Examinations**

    📚 **Library**

    🏠 **Hostel**

    🎓 **Scholarships**

    💼 **Placements**

    📞 **Student Support**
    """)

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()


# ---------- CHAT HISTORY ----------

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------- DISPLAY OLD MESSAGES ----------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# ---------- USER INPUT ----------

user_question = st.chat_input(
    "Ask your student support question..."
)


# ---------- CHATBOT RESPONSE ----------

if user_question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):
        st.write(user_question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                answer = get_response(user_question)

                st.write(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as e:

                st.error(
                    "The chatbot could not process your request. "
                    "Please check the Gemini API configuration."
                )
