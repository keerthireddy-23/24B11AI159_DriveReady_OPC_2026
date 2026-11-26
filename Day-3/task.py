!pip install -q -U langchain langchain-google-genai
import os
from google.colab import userdata

os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.3
)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

SYSTEM = """ROLE:   You are the friendly assistant for Sweet Crumbs Home Bakery.
FACTS:  Plum cake Rs 500. Chocolate cake Rs 650. Cupcake Rs 80 each.
        Orders need 24 hours' notice. All cakes have eggless versions.
RULES:  Never promise a delivery time or place. If it isn't in FACTS,
        say "I'll check with the owner." Work out totals carefully.
FORMAT: Under 50 words, friendly, English or Telugu matching the customer."""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM),
    MessagesPlaceholder("history"),
    ("human", "{question}"),
])

chain = prompt | llm | StrOutputParser()

history = []

def ask(question: str) -> str:
    answer = chain.invoke({"history": history, "question": question})
    history.extend([("human", question), ("ai", answer)])
    return answer

print(ask("Hi, I'm Ravi. Do you make eggless cakes?"))
print(ask("What's my name?"))
import csv

def run_tests(path: str = "/content/test.csv") -> None:
    rows = list(csv.DictReader(open(path)))
    passed = 0

    for row in rows:
        answer = chain.invoke({"history": [], "question": row["question"]})
        ok = row["must_include"].lower() in answer.lower()
        passed += ok
        print("PASS" if ok else "FAIL", "|", row["question"], "→", answer[:70])

    print(f"\n{passed}/{len(rows)} passed ({passed / len(rows):.0%})")
  from langchain.agents import create_agent

agent_order = create_agent(model=llm, tools=[], system_prompt=SYSTEM)  # tools come tomorrow

result_order = agent_order.invoke({"messages": [{"role": "user", "content": "Do you make eggless cakes?"}]})

print(result_order["messages"][-1].content)
