from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("OPENAI_API_KEY")
assert api_key, "OPENAI_API_KEY not set in .env file!"

memory = ConversationBufferWindowMemory(k=3, return_messages=True)

conversation = ConversationChain(
    llm=ChatOpenAI(temperature=0, openai_api_key=api_key),
    memory=memory,
    verbose=True
)


def print_memory():
    for msg in memory.chat_memory.messages:
        print(f"{msg.type.upper()}: {msg.content}")
