import os
from dotenv import load_dotenv

from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings


load_dotenv()


embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vector_store = PineconeVectorStore(
    embedding=embedding,
    index_name=os.environ["INDEX_NAME"]
)


retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)