from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

class SearchService:
    def __init__(self):
        api_key = os.getenv("TAVILY_API_KEY")
        if api_key:
            self.client = TavilyClient(api_key=api_key)
        else:
            self.client = None

    async def search(self, query: str):
        if not self.client:
            return "Search API key not configured."
        
        response = self.client.search(query=query, search_depth="advanced")
        return response['results']

search_service = SearchService()
