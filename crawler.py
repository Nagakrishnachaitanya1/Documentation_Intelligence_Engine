import asyncio

from langchain_tavily import TavilyCrawl
from dotenv import load_dotenv

load_dotenv()
async def crawler(url:str):
    
    
    crawler_url = TavilyCrawl()
    
    data =await crawler_url.ainvoke({
        "url" : url,
        "max_depth" : 5,
        "extract_depth" : "advanced",
        # "instructions" : query
    })
    
    return data


if __name__ == "__main__":
    asyncio.run(crawler("https://docs.langchain.com/oss/python/langchain/overview"))
    # asyncio.run(crawler("https://docs.langchain.com/oss/python/langchain/overview","find about : LangChain agents"))

