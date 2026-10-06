# from rag import chain

# query = "what is langchain agents"

# print(chain.invoke({"question": query}))

from rag import chain
from vector_store import retriever

query = "What is middleware in LangChain?"

docs = retriever.invoke(query)

for i, doc in enumerate(docs, start=1):
    print(f"\n--- Retrieved Chunk {i} ---")
    print(doc.page_content)
    print("Source:", doc.metadata.get("source"))

print("\n--- FINAL ANSWER ---")
print(chain.invoke({"question": query}))