from operator import itemgetter

from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from vector_store import retriever


llm = ChatGroq(
    model="openai/gpt-oss-20b"
)


def combine(documents):
    return "\n\n".join(
        document.page_content
        for document in documents
    )


prompt = ChatPromptTemplate.from_template(
    """
    Answer the question based only on the following context:

    {context}

    Question: {question}

    Provide a detailed answer:
    """
)


chain = (
    RunnablePassthrough.assign(
        context=itemgetter("question") | retriever | combine
    )
    | prompt
    | llm
    | StrOutputParser()
)

