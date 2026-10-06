from rag import chain

query = "what is langchain agents"

print(chain.invoke({"question": query}))
