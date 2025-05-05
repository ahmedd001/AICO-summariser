from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader

from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("OPENAI_API_KEY")
assert api_key, "OPENAI_API_KEY not set in .env file!"

def fetch_web_content(url):
    """Fetch content from the webpage using LangChain's WebBaseLoader."""
    try:
        loader = WebBaseLoader(url)
        docs = loader.load()
        if not docs:
            raise ValueError("No content fetched from the webpage.")
        content = docs[0].page_content
        return content
    except Exception as e:
        print(f"Error fetching content: {e}")
        return ""

def summarize_web_content(text):
    """Summarize the content using LangChain summarization."""
    llm = ChatOpenAI(openai_api_key=api_key, temperature=0, model_name="gpt-3.5-turbo")
    chain = load_summarize_chain(llm, chain_type="stuff")
    docs = [Document(page_content=text)]
    result = chain.invoke(docs)
    
    if isinstance(result, dict):
        summary = result.get("output_text", "")
    else:
        summary = str(result)

    print(f"Clean summary: {summary}")
    return summary

def extract_main_topic(summary_text):
    """Use LLM to generate a professional topic/title from the summary."""
    if not summary_text:
        return "No topic available."

    llm = ChatOpenAI(openai_api_key=api_key, temperature=0, model_name="gpt-3.5-turbo")

    prompt = (
        "Based on the following summary of a webpage, generate a professional and concise title "
        "that captures the main topic:\n\n"
        f"{summary_text}\n\nTitle:"
    )

    response = llm.invoke(prompt)
    topic = response.content.strip().replace('"', '')  
    print(f"Generated professional title: {topic}")
    return topic





