import streamlit as st
import joblib
import string

# Define the tokenizer function BEFORE loading vectorizer
def custom_tokenizer(text):
    return text.split(",")

# Load model and vectorizer
model = joblib.load("faq_model2.pkl")
vectorizer = joblib.load("faq_vectorizer2.pkl")

# Clean user input
def clean_text(text):
    text = text.lower()
    return text.translate(str.maketrans("", "", string.punctuation))

# Set up app
st.set_page_config(page_title="FAQ Chatbot", layout="centered")
st.markdown("<h2 style='text-align: center;'>💬 DASSOFT FAQ Chatbot</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>How can I help you?</p>", unsafe_allow_html=True)
st.divider()

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_query = st.chat_input("You:", key="input")

if user_query:
    # Clean and predict
    user_query_clean = clean_text(user_query)
    user_vector = vectorizer.transform([user_query_clean])
    bot_response = model.predict(user_vector)[0]

    # Add messages to history
    st.session_state.chat_history.append(("user", user_query))
    st.session_state.chat_history.append(("bot", bot_response))

# Display chat history
for sender, msg in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"<div style='text-align: right; background-color: #36454F; padding: 10px; border-radius: 10px; margin: 5px 0 5px auto; max-width: 80%;'>{msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; background-color: #1B1212; padding: 10px; border-radius: 10px; margin: 5px auto 5px 0; max-width: 80%;'>🤖 {msg}</div>", unsafe_allow_html=True)

# Optional: Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []