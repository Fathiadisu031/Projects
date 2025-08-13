import os
from dotenv import load_dotenv
from pathlib import Path
import streamlit as st

from huggingface_hub import InferenceClient

# dotenv_path = Path(r'C:\Users\Hp\Desktop\Chatbox\.env')
# load_dotenv(dotenv_path=dotenv_path)
load_dotenv(r"C:\Users\Hp\Desktop\Chatbox\.env")
 
HUGGINGFACE_TOKEN = os.getenv("HF_TOKEN")
#print(f"HUGGINGFACE_TOKEN: {HUGGINGFACE_TOKEN}")


client = InferenceClient(
    token=HUGGINGFACE_TOKEN,
    model="mistralai/Mistral-7B-Instruct-v0.2"
    )

# Streamlit interface

# page layout
st.set_page_config(page_title='Your Bestie', page_icon="💬", layout="centered")
st.title("Female Health Bestfriend 🌸💖")
st.subheader("I'm here to help you understand everything about your body and health, just like your best friend would!")
#st.image("banner.png", use_container_width=True)
st.write("Ask me anything!!")
# User input
user_input = st.text_input("Type your question here...")
if user_input.strip():
    messages =[
        {"role" : "system", "content" : "You are a female bestfriend who explains female health questions clearly. Give a well decriptive summary about what is being asked and show cases or examples if possible."},
        {"role" : "user" , "content" : user_input}]
    try : 
        with st.spinner("Thinking..."):
            response = client.chat_completion(messages = messages,
                                              max_tokens=1000,
                                              temperature=0.7)
        st.write("**Assistant:**", response.choices[0].message.content)
    except Exception as error:
        st.error(f"An error occurred: {error}")
    
    
    
    
