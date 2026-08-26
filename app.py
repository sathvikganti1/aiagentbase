import os

from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv


# Load .env
load_dotenv()


# Create Flask application
app = Flask(__name__)


# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing!")


# Connect to Groq
client = Groq(api_key=api_key)


# Conversation memory
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Chat API
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message")

    if not user_message:
        return jsonify({
            "error": "Message is empty"
        }), 400


    # Add user message
    messages.append({
        "role": "user",
        "content": user_message
    })


    # Ask Groq
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )


    # Get AI response
    answer = response.choices[0].message.content


    # Save AI response
    messages.append({
        "role": "assistant",
        "content": answer
    })


    return jsonify({
        "response": answer
    })


# Start server
if __name__ == "__main__":
    app.run(debug=True)