
# Install required library
!pip install -q langchain-groq

# Imports
import json
import functools
from google.colab import userdata
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Initialize Groq model
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.3,
    groq_api_key=userdata.get("GROQ_API_KEY")
)

MODEL = "openai/gpt-oss-20b"

# Bakery menu
MENU = {
    "plum cake": 500,
    "chocolate cake": 650,
    "cupcake": 80
}

# System prompt
SYSTEM = f"""ROLE: You are the friendly assistant for Sweet Crumbs Home Bakery.

FACTS:
Menu with prices in rupees: {json.dumps(MENU)}
Orders need 24 hours' notice.
All cakes have eggless versions.

RULES:
Never promise a delivery time.
If it isn't in FACTS, say "I'll check with the owner."
Remember the customer's name and order during the chat.

FORMAT:
Under 50 words, friendly, English or Telugu matching the customer.
"""

# Logging decorator
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"   [log] {func.__name__}{args} -> {result!r}")
        return result
    return wrapper

# Price calculation
@log_call
def get_price(item: str, qty: int = 1) -> int:
    """Return the total price in rupees for qty of an item."""
    item = item.lower().strip()

    if item not in MENU:
        raise ValueError("Item not available in the menu.")

    if qty <= 0:
        raise ValueError("Quantity must be positive.")

    return MENU[item] * qty

# Chat history
history = [
    SystemMessage(content=SYSTEM)
]

MAX_TURNS = 8

# Chat function
def chat(user_text: str) -> str:

    history.append(HumanMessage(content=user_text))

    recent = [history[0]] + history[1:][-MAX_TURNS:]

    try:
        response = llm.invoke(recent)
        reply = response.content

    except Exception as e:
        print("Error:", e)
        reply = "Sorry! Something went wrong. Please try again."

    history.append(AIMessage(content=reply))

    return reply

# Test price calculation
print("Total for 6 cupcakes:", get_price("cupcake", 6))

# Start chatbot
print("\nWelcome to Sweet Crumbs Home Bakery!")
print("Type 'bye' to exit.\n")

while True:

    text = input("You: ")

    if text.lower().strip() in ("bye", "exit", "quit"):
        print("Bot: Thank you for visiting Sweet Crumbs!")
        break

    if not text.strip():
        continue

    print("Bot:", chat(text))
