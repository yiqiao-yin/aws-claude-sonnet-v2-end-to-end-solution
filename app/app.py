import streamlit as st
import os
from helper import invoke_text_api, invoke_text_image_api
import base64

# Set Streamlit page config to wide layout
st.set_page_config(page_title="Chatbot", layout="wide")

# App Title with Emoji
st.title("🤖 Chatbot with Image Support 🖼️")

# Sidebar for Image Upload
st.sidebar.header("📂 Upload an Image (Optional)")
uploaded_file = st.sidebar.file_uploader("📸 Upload an image", type=["png", "jpg", "jpeg"])

# If an image is uploaded, display it in the sidebar
if uploaded_file:
    st.sidebar.image(uploaded_file, caption="🖼️ Uploaded Image Preview", use_container_width=True)

# Sidebar Parameters for AI Model
st.sidebar.header("⚙️ Model Parameters")

max_tokens = st.sidebar.slider("📝 Max Tokens (Response Length)", 100, 2000, 1000)
temperature = st.sidebar.slider("🔥 Temperature (Creativity)", 0.0, 1.0, 0.7)
top_k = st.sidebar.slider("🎯 Top K (Diversity Filter)", 1, 500, 150)
top_p = st.sidebar.slider("📊 Top P (Probability Sampling)", 0.0, 1.0, 0.98)

# Button to clear chat history
if st.sidebar.button("🗑️ Clear Chat History"):
    st.session_state.messages = []  # Reset conversation history
    st.rerun()  # Corrected method to refresh the app

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("What would you like to ask? 🤔"):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call the appropriate API function based on input type
    with st.spinner("🤖 Thinking..."):
        if uploaded_file:
            # Convert uploaded image to Base64
            image_bytes = uploaded_file.read()
            base64_image = base64.b64encode(image_bytes).decode("utf-8")
            response = invoke_text_image_api(base64_image, prompt, max_tokens, temperature, top_k, top_p)
        else:
            response = invoke_text_api(prompt, max_tokens, temperature, top_k, top_p)

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})