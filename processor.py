import asyncio
import os
from dotenv import load_dotenv

from langchain_core.documents import Document
from crawler import crawler

from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore


load_dotenv()

url = "https://docs.langchain.com/oss/python/langchain/overview"

query = "find about : LangChain agents"

async def processor(url: str,query:str):
    
    data = await crawler(url,query)
    
    all_docs = [
        Document(
        page_content = result["raw_content"],
        metadata = {"source" : result["url"]}
        )  
        for result in data["results"]
        if result.get("raw_content")
        ]
    return all_docs

docs = asyncio.run(processor(url,query))

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 5
)

chunks = splitter.split_documents(docs)

Hugging_Face_embedding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-minilm-l6-v2"
)

vectorstore = PineconeVectorStore.from_documents(documents = chunks,embedding = Hugging_Face_embedding,index_name = os.environ["INDEX_NAME"])

print("completed!!!!")