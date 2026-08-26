import os

from groq import Groq
from dotenv import load_dotenv


# Load variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing!")


# Connect to Groq
client = Groq(api_key=api_key)


# Conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]


print("=" * 50)
print("             MY GROQ AI")
print("=" * 50)
print("Type 'bye' to quit.")
print()


while True:

    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("AI: Goodbye!")
        break

    # Add user's message
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Send request to Groq
    response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=messages
)

    # Get AI response
    answer = response.choices[0].message.content

    print("\nAI:", answer)
    print()

    # Save AI response
    messages.append({
        "role": "assistant",
        "content": answer
    })