import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("Google_API_KEY")

# Set up the Streamlit App
st.set_page_config(page_title="OCR Chatbot", layout="wide")
st.title("Multimodal ChatBot")
st.caption("ChatBot that can answer queries for text and images")

# Set up the Gemini model
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

 # Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

    # Sidebar for image upload
with st.sidebar:
    st.title("Chat with Images")
    uploaded_file = st.camera_input("Take a picture !!")
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    # Main layout
chat_placeholder = st.container()
with chat_placeholder:
    # Display the chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input area at the bottom
prompt = st.chat_input("What do you want to know?")

if prompt:
    inputs = [prompt]
        
        # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
    with chat_placeholder:
        with st.chat_message("user"):
                st.markdown(prompt)
        
    if uploaded_file:
        inputs.append(image)

    with st.spinner('Generating response...'):
            # Generate response
        response = model.generate_content(inputs)
    
        # Display assistant response in chat message container
    with chat_placeholder:
        with st.chat_message("assistant"):
            st.markdown(response.text)

if uploaded_file and not prompt:
    st.warning("enter a text query")
