import os
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import pyttsx3
import speech_recognition as sr

# Load environment variables from .env
load_dotenv()

# Azure OpenAI credentials
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_API_BASE")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

# Load text files
def load_text_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

chat_patterns = load_text_file("chat_patterns.txt")
context_flow = load_text_file("context_flow.txt")
restaurant_kb = load_text_file("restaurant_kb.txt")

# Prompt Template
custom_template = f"""
You are a warm, polite, and helpful AI voice assistant for a restaurant.

### Guidelines
{context_flow}

### Knowledge Base
{restaurant_kb}

### Sample Chat Patterns
{chat_patterns}

Use the patterns above to understand user intent, provide natural responses, and follow the context flow logic.

Conversation history:
{{history}}
Customer: {{input}}
Assistant:"""

prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=custom_template,
)

# Memory
memory = ConversationBufferMemory()
# memory.clear()

# LangChain LLM
llm = AzureChatOpenAI(
    openai_api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    deployment_name=AZURE_OPENAI_DEPLOYMENT_NAME,
    api_version=AZURE_OPENAI_API_VERSION,
    temperature=0.5
)

# Conversation Chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=False
) 

# Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)

# Set female voice
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower():  # "Zira" is a common female voice on Windows
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech Recognizer
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("😕 Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        print("❌ Speech service is unavailable.")
        return None

# Main loop
def main():
    speak("Hi, Welcome to the Joni eats! How can I help you today?")
    while True:
        user_input = listen()
        if user_input:
            if "bye" in user_input.lower() or "goodbye" in user_input.lower() or "end call" in user_input.lower() or "have a day" in user_input.lower():
                speak("You're welcome! Have a great day!")
                break
            response = conversation.predict(input=user_input)
            print(f"🤖 Assistant: {response}")
            speak(response)

if __name__ == "__main__":
    main()
