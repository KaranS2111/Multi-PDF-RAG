import gradio as gr
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable")

genai.configure(api_key=GOOGLE_API_KEY)

# Create the generative model
model = genai.GenerativeModel('gemini-pro')

def generate_response(prompt):
    try:
        # Generate content using the Gemini model
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"


def create_gemini_interface():
    interface = gr.Interface(
        fn=generate_response,
        inputs=gr.Textbox(
            label="Enter your prompt", 
            placeholder="Type your question or request here..."
        ),
        outputs=gr.Textbox(
            label="Gemini Response", 
            placeholder="Response will appear here..."
        ),
        title="Gemini AI Chatbot",
        description="A simple interface to interact with Google's Gemini AI",
        theme="default",
        examples=[
            ["Write a short poem about technology"],
            ["Explain quantum computing in simple terms"],
            ["Create a meal plan for a vegetarian diet"]
        ]
    )
    
    return interface


if __name__ == "__main__":
    app = create_gemini_interface()
    app.launch()