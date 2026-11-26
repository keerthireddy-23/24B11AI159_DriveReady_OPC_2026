
# Day 1 - Sweet Crumbs Home Bakery Chatbot

!pip install -q openai

from google.colab import userdata
from openai import OpenAI

api_key = userdata.get("GROQ_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "openai/gpt-oss-20b"


response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a funny joker"},
        {"role": "user", "content": "Tell me a joke"}
    ]
)

print("Joke:")
print(response.choices[0].message.content)


SYSTEM = """
ROLE: You are the assistant for Sweet Crumbs Home Bakery.

FACTS:
We bake to order. Orders need 24 hours' notice.
All cakes have eggless versions.
Plum cake Rs 500.
Chocolate cake Rs 650.
Cupcake Rs 80.

RULES:
Never promise a delivery time.
If the answer isn't in FACTS, say "I'll check with the owner."
FORMAT: Under 50 words, friendly, English or Telugu matching the customer.
"""

response = client.chat.completions.create(
    model=MODEL,
    temperature=0.2,
    messages=[
        {"role": "system", "content": SYSTEM},
        {
            "role": "user",
            "content": "Can I get an eggless cake today evening?"
        }
    ]
)

print("\nBakery Chatbot:")
print(response.choices[0].message.content)

print("\nToken Usage:")
print(response.usage)
