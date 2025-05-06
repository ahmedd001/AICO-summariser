from langchain.prompts import PromptTemplate

# System prompt for the conversation chain
SYSTEM_PROMPT = """You are an AI assistant specialized in web content analysis and summarization. 
Your goal is to provide clear, concise, and meaningful summaries while maintaining context awareness.
Focus on extracting key information and maintaining a professional tone."""

# Template for initial content summarization
SUMMARY_TEMPLATE = """Please analyze the following web content and provide a comprehensive summary.
Focus on the main points, key arguments, and important details while maintaining clarity and coherence.

Content:
{text}

Summary:"""

# Template for topic extraction
TOPIC_TEMPLATE = """Based on the following summary, identify the main topic or theme.
The topic should be concise, specific, and capture the essence of the content.

Summary:
{summary}

Main Topic:"""

# Template for content analysis
ANALYSIS_TEMPLATE = """Analyze the following content and provide insights on:
1. Main arguments or points
2. Supporting evidence
3. Key takeaways
4. Potential implications

Content:
{content}

Analysis:"""

# Create PromptTemplate objects
summary_prompt = PromptTemplate(
    input_variables=["content"],
    template=SUMMARY_TEMPLATE
)

topic_prompt = PromptTemplate(
    input_variables=["summary"],
    template=TOPIC_TEMPLATE
)

analysis_prompt = PromptTemplate(
    input_variables=["content"],
    template=ANALYSIS_TEMPLATE
) 