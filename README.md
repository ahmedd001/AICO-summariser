# AICO Web Content Summarizer

A  web content summarization tool built with FastAPI and LangChain, utilizing OpenAI's GPT models for intelligent content processing and conversation management.

##  Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Setup Instructions

1. **Clone the Repository**
```bash
git clone git@github.com:ahmedd001/AICO-summariser.git
cd AICO-summariser
```

2. **Create Virtual Environment**
```bash
python3 -m venv aicoenv
source aicoenv/bin/activate  # On Windows: aicoenv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt # there are unused dpependices but its better to get them
```

4. **Configure Environment**
- Create a `.env` file in the root directory
- Add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

5. **Run the Application**
```bash
uvicorn src.api.routes:app --reload
```

6. **Access the API**
- API Documentation: http://127.0.0.1:8000/docs
- Base URL: http://127.0.0.1:8000

## 📚 Project Structure

```
src/api/routes.py #FASTAPI ENDPOINTS
├── api/
│   └── routes.py          # FastAPI routes and endpoints
└── services/
    ├─- summarizer.py      # Web content processing
    └── memory.py          # Conversation management
```

## 🛠 API Endpoints

### POST /summarize
Summarizes web content with two modes:
1. **URL Mode**: Provide a URL to get content summary and main topic
2. **Question Mode**: Ask questions about previously summarized content

Example request:
```json
{
    "url": "https://example.com",
    "question": "What is the main topic?"//only url will also work,question is optional but useful
}
```

### GET /memory    (optinal endpoint not specified in the task)                    
Retrieves conversation history and previous interactions.   

## 🧠 Project Explanation

This project combines several powerful technologies to create an intelligent web content summarization system:

### Core Features

1. **Web Content Processing**
   - Fetches content from any URL using LangChain's WebBaseLoader
   - Processes HTML content intelligently
   - Extracts meaningful text while filtering out noise

2. **Smart Summarization**
   - Uses OpenAI's GPT-3.5-turbo model
   - Generates concise, coherent summaries
   - Extracts main topics and key points

3. **Conversation Memory**
   - Maintains context across multiple interactions
   - Allows follow-up questions about summarized content
   - Uses LangChain's memory management system

   **PROMPT ENGINEERING**
   - Included a system prompt that goes in with every request
   - To imorove the response and make it more meaningful

### Technical Implementation

- **FastAPI Framework**: High-performance async web framework
- **LangChain Integration**: 
  - Document loading and processing
  - Chain management for complex operations
  - Memory management for conversations
- **OpenAI GPT Models**: 
  - Content summarization
  - Topic extraction
  - Question answering




