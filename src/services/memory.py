from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from src.config import settings

# Load environment variables from root .env file
load_dotenv()

# Initialize memory with window size from settings
memory = ConversationBufferWindowMemory(
    k=settings.MEMORY_WINDOW_SIZE,
    return_messages=True
)

# Initialize conversation chain
conversation = ConversationChain(
    llm=ChatOpenAI(
        openai_api_key=settings.OPENAI_API_KEY,
        temperature=settings.OPENAI_TEMPERATURE,
        model_name=settings.OPENAI_MODEL,
        max_tokens=settings.MAX_OUTPUT_TOKENS
    ),
    memory=memory,
    verbose=True
)
