import streamlit as st
import google.generativeai as genai

# Set up Gemini API key
genai.configure(api_key="AIzaSyBUsXmmFh0E5DcwX15uwY9rzgb_ZPsa5V4")

# Chatbot function (Updated for Gemini API)
def chat_with_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")  # Use the latest model
    response = model.generate_content(prompt)
    return response.text

# Streamlit App UI
st.title("🤖 Free AI Chatbot (Powered by Gemini)")
st.write("Ask me anything!")

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = chat_with_gemini(user_input)
        st.text_area("AI:", response, height=200)
    else:
        st.warning("Please enter a message.")
