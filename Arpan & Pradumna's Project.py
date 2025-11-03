# A powerful, AI-driven chatbot using the Google Generative AI API

# First, you must install the library:
# In the Visual Studio terminal, type: pip install google-generativeai

import google.generativeai as genai
import os

# --- Configuration ---
# IMPORTANT: You must get your own API Key.
# 1. Go to https://aistudio.google.com/app/apikey
# 2. Create an API key and copy it.
# 3. Paste your key below. (For real projects, use environment variables)
try:
    genai.configure(api_key="AIzaSyDeJD8iL52GsqkbJ-VK1JfYa6HNfJ7c9T8")
except AttributeError:
    print("Error: The 'google.generativeai' library is not installed.")
    print("Please install it by running: pip install google-generativeai")
    exit()

# Create the model
model = genai.GenerativeModel('gemini-2.5-pro')

def main_chatbot():
    print("🤖 Hello! I am an advanced chatbot.")
    print("I can help with math, physics, and medical questions.")
    print("Type 'bye' to exit.")

    # Create a new chat session
    chat = model.start_chat(history=[])

    while True:
        user_input = input("You: ")

        if "bye" in user_input.lower():
            print("Bot: Goodbye! Stay curious. 💡")
            break

        try:
            # Send the user's message to the model
            response = chat.send_message(user_input)
            
            # Print the model's response
            print(f"Bot: {response.text}")

        except Exception as e:
            print(f"An error occurred: {e}")
            print("Sorry, I couldn't process that. Please try again.")

# Run the chatbot
if __name__ == "__main__":
    main_chatbot()