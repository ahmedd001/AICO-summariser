from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # OpenAI Configuration
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-3.5-turbo"
    OPENAI_TEMPERATURE: float = 0.0
    
    # Token Limits
    MAX_INPUT_TOKENS: int = 3800  # Reduced to account for system prompt
    MAX_OUTPUT_TOKENS: int = 1000
    MAX_SUMMARY_LENGTH: int = 500
    
    # Memory Configuration
    MEMORY_WINDOW_SIZE: int = 3
    
    # Content Processing
    MIN_CONTENT_LENGTH: int = 100
    MAX_CONTENT_LENGTH: int = 9000  # Reduced to account for prompts
    
    # API Configuration
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_DEBUG: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() 