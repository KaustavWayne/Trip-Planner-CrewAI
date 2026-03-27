from crewai.tools import tool
from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search_web(query: str) -> str:
    """
    Perform a SINGLE web search query to get travel information.

    IMPORTANT:
    - Use only ONE query
    - Combine weather, attractions, and cost in one query
    - Do NOT call multiple times

    Example:
    "Tokyo travel weather attractions cost budget"
    """
    response = client.search(query=query, max_results=5)
    results = response.get("results", [])

    return "\n".join([
        f"{i+1}. {r['title']} - {r['content'][:150]}"
        for i, r in enumerate(results)
    ])