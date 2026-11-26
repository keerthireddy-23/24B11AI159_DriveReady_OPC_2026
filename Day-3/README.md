# Day 3 – AI Agent Development Using LangChain and Gemini

## Project Overview

This project demonstrates the development of a simple AI-powered chatbot for **Sweet Crumbs Home Bakery** using LangChain and Google's Gemini model.

The chatbot acts as a virtual bakery assistant. It answers customer questions about cake prices, eggless options, order requirements, and remembers information from previous messages.

## Technologies Used

- Python
- Google Colab
- LangChain
- LangChain Google GenAI
- Google Gemini API
- CSV (for automated testing)

## Features

1. **AI-powered chatbot:** Uses Google's Gemini model to generate natural-language responses.
2. **Custom system prompt:** Defines the chatbot's role, bakery information, response rules, and language preferences.
3. **Conversation history:** Remembers previous messages and uses them to answer follow-up questions.
4. **Product information:** Provides cake prices and eggless cake availability.
5. **Order guidelines:** Informs customers that orders require 24 hours' notice.
6. **Automated testing:** Checks chatbot responses against predefined test cases.
7. **LangChain agent:** Creates a basic agent using `create_agent`, preparing the foundation for adding tools in future tasks.

## Bakery Information

| Product | Price |
|---|---:|
| Plum Cake | Rs 500 |
| Chocolate Cake | Rs 650 |
| Cupcake | Rs 80 each |

Additional information:
- All cakes have eggless versions.
- Orders require 24 hours' notice.
- Delivery details not included in the available bakery facts are referred to the owner.

## Implementation

### 1. Install Dependencies

```python
!pip install -q -U langchain langchain-google-genai
```

### 2. Configure Gemini

The Gemini API key is accessed securely using Google Colab Secrets.

```python
from google.colab import userdata
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.3
)
```

### 3. Create the Chatbot Prompt

Used `ChatPromptTemplate` and `MessagesPlaceholder` to define the chatbot's instructions and conversation history.

### 4. Implement Conversation Memory

Created an `ask()` function that:
- Accepts customer questions.
- Sends the question and conversation history to the chain.
- Generates a response.
- Updates conversation history.

### 5. Automated Testing

Created a `run_tests()` function that reads test cases from a CSV file and checks whether the expected information appears in chatbot responses.

## Sample Interaction

**Customer:** Hi, I'm Ravi. Do you make eggless cakes?

**Chatbot:** Hi Ravi! Yes, we offer eggless versions for all our cakes.

**Customer:** What's my name?

**Chatbot:** Your name is Ravi!

This demonstrates that the chatbot can retain information from previous messages.

## Test Results

The chatbot was tested using five test cases.

| Test Case | Result |
|---|---|
| Plum cake price | PASS |
| Eggless cake availability | PASS |
| Same-day order request | PASS |
| Delivery location enquiry | PASS |
| Price of 6 cupcakes | PASS |

**Overall Result: 5/5 test cases passed (100%).**

## LangChain Agent

A basic agent was created using LangChain's `create_agent()` function.

```python
from langchain.agents import create_agent

agent_order = create_agent(
    model=llm,
    tools=[],
    system_prompt=SYSTEM
)
```

Currently, the agent has no external tools. It establishes the basic structure for extending the chatbot with additional capabilities.

## Key Learnings

- Understanding LangChain and its components.
- Connecting Google Gemini with LangChain.
- Creating custom system prompts.
- Using conversation history for contextual responses.
- Building chains using the LCEL pipeline.
- Implementing automated chatbot testing.
- Creating a basic AI agent using `create_agent()`.

## Future Enhancements

- Add tools for checking product availability.
- Implement order placement functionality.
- Integrate a bakery order database.
- Add customer order tracking.
- Support more languages.
- Connect the chatbot to a real bakery ordering system.

## Conclusion

This project helped demonstrate how to build a conversational AI chatbot using LangChain and Google Gemini. It covers prompt engineering, conversation memory, automated testing, and the initial implementation of an AI agent.
