import streamlit as st
import pandas as pd

# MUST be the first Streamlit command
st.set_page_config(page_title="Dassoft FAQ Bot", layout="centered")

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("faq_dataset.csv")

faq_df = load_data()

# Parse keywords
faq_responses = []
for _, row in faq_df.iterrows():
    try:
        keywords = eval(row["Question_Keywords"])
        if isinstance(keywords, list):
            keywords = [kw.lower().strip() for kw in keywords]
            faq_responses.append((keywords, row["Answers"]))
    except:
        continue

# Chat-style title
st.title("💬 Dassoft FAQ Chatbot")
st.caption("I'm here to help you with your questions. How can I assist you today?")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask your question here...")
if user_input:
    # Show user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Match logic
    input_words = set(user_input.lower().split())
    best_match = None
    highest_score = 0

    for keywords, response in faq_responses:
        match_score = len(input_words.intersection(set(keywords)))
        if match_score > highest_score:
            highest_score = match_score
            best_match = response

    # Response logic
    if best_match and highest_score > 0:
        bot_reply = best_match
    else:
        bot_reply = "❌ Sorry, I couldn't find an answer. Please try rephrasing your question."

    # Show bot's message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

# Add a button to clear chat history
if st.button("🗑️ Clear Chat History"):
    st.session_state.messages = []
    st.rerun()

# Add a footer
st.markdown(
    """
    <style>
        footer {
            visibility: hidden;
        }
        footer:after {
            content: 'Made with ❤️ by Dassoft';
            visibility: visible;
            display: block;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            color: #999;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)