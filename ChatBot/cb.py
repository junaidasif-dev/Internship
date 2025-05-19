import streamlit as st
import pandas as pd

# Load default FAQs
faq_df = pd.read_csv("faq_dataset.csv")  # Replace with the path to your CSV file

# Separate default FAQs and keyword responses based on column names
keyword_faqs = faq_df[faq_df.columns.intersection(["Question_Keywords", "Answers"])]

# Process keyword entries into a list of tuples (list of keywords, response)
faq_responses = []
if "Question_Keywords" in keyword_faqs and "Answers" in keyword_faqs:
    for _, row in keyword_faqs.iterrows():
        keywords = [kw.strip().lower() for kw in row["Question_Keywords"].split(",")]
        faq_responses.append((keywords, row["Answers"]))

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("💬 Dassoft FAQ Chatbot")

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask your question here...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    query = user_input.lower()
    found = False
    for keywords, response in faq_responses:
        if all(word in query for word in keywords):
            bot_reply = response
            found = True
            break

    if not found:
        bot_reply = "❌ Sorry, I couldn't find an answer. Please try rephrasing your question."

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
