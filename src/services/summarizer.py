from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate

from bs4 import BeautifulSoup
from dotenv import load_dotenv

from src.config import settings
from src.templates.prompts import (
    summary_prompt,
    topic_prompt,
    analysis_prompt,
    SYSTEM_PROMPT
)

# Load environment variables from root .env file
load_dotenv()

def fetch_web_content(url):
    """Fetch content from the webpage using LangChain's WebBaseLoader."""
    try:
        loader = WebBaseLoader(url)
        docs = loader.load()
        if not docs:
            raise ValueError("No content fetched from the webpage.")
        
        # Clean and preprocess content
        content = docs[0].page_content
        content = clean_content(content)
        
        # Split content if it exceeds token limit
        if len(content) > settings.MAX_CONTENT_LENGTH:
            content = split_content(content)
            
        return content
    except Exception as e:
        print(f"Error fetching content: {e}")
        return ""

def clean_content(content):
    """Clean and preprocess the content."""
    # Remove extra whitespace
    content = ' '.join(content.split())
    
    # Remove HTML tags if any
    soup = BeautifulSoup(content, 'html.parser')
    content = soup.get_text()
    
    return content

def split_content(content):
    """Split content into chunks if it exceeds the maximum length."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.MAX_CONTENT_LENGTH,
        chunk_overlap=200
    )
    chunks = text_splitter.split_text(content)
    return chunks[0]  # Return first chunk for now

def summarize_web_content(text):
    """Summarize the content using LangChain summarization with custom prompt."""
    llm = ChatOpenAI(
        openai_api_key=settings.OPENAI_API_KEY,
        temperature=settings.OPENAI_TEMPERATURE,
        model_name=settings.OPENAI_MODEL,
        max_tokens=settings.MAX_OUTPUT_TOKENS
    )
    
    # Create a new prompt template that matches the expected input variable
    chain_prompt = PromptTemplate(
        input_variables=["text"],
        template=f"{SYSTEM_PROMPT}\n\n{summary_prompt.template}"
    )
    
    # Use custom prompt template
    chain = load_summarize_chain(
        llm,
        chain_type="stuff",
        prompt=chain_prompt
    )
    
    docs = [Document(page_content=text)]
    result = chain.invoke(docs)
    
    if isinstance(result, dict):
        summary = result.get("output_text", "")
    else:
        summary = str(result)

    # Ensure summary length is within limits
    if len(summary) > settings.MAX_SUMMARY_LENGTH:
        summary = summary[:settings.MAX_SUMMARY_LENGTH] + "..."
        
    print(f"Generated summary: {summary}")
    return summary

def extract_main_topic(summary_text):
    """Use LLM to generate a professional topic/title from the summary."""
    if not summary_text:
        return "No topic available."

    llm = ChatOpenAI(
        openai_api_key=settings.OPENAI_API_KEY,
        temperature=settings.OPENAI_TEMPERATURE,
        model_name=settings.OPENAI_MODEL,
        max_tokens=100  # Limit topic length
    )

    # Create a prompt with system message and topic extraction
    prompt = PromptTemplate(
        input_variables=["summary"],
        template=f"{SYSTEM_PROMPT}\n\n{topic_prompt.template}"
    )

    # Use custom prompt template
    result = llm.invoke(prompt.format(summary=summary_text))
    topic = result.content.strip().replace('"', '')
    
    print(f"Generated topic: {topic}")
    return topic

def analyze_content(content):
    """Perform detailed content analysis."""
    llm = ChatOpenAI(
        openai_api_key=settings.OPENAI_API_KEY,
        temperature=settings.OPENAI_TEMPERATURE,
        model_name=settings.OPENAI_MODEL,
        max_tokens=settings.MAX_OUTPUT_TOKENS
    )
    
    # Create a prompt with system message and analysis
    prompt = PromptTemplate(
        input_variables=["content"],
        template=f"{SYSTEM_PROMPT}\n\n{analysis_prompt.template}"
    )
    
    # Use custom analysis prompt
    result = llm.invoke(prompt.format(content=content))
    analysis = result.content.strip()
    
    return analysis





