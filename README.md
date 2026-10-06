# DocuRAG 📚

DocuRAG is a Retrieval-Augmented Generation (RAG) mini-project that crawls documentation, processes and embeds the extracted content, stores it in a Pinecone vector database, retrieves relevant chunks, and uses an LLM to answer questions based on the retrieved context.

## Architecture

```text
Documentation URL
       ↓
Tavily Crawl
       ↓
LangChain Documents
       ↓
Text Chunking
       ↓
HuggingFace Embeddings
       ↓
Pinecone Vector Database
       ↓
Similarity Retrieval
       ↓
Relevant Documents
       ↓
Context + User Question
       ↓
Groq LLM
       ↓
Final Answer
```

## Tech Stack

- Python
- LangChain
- Tavily
- Hugging Face Sentence Transformers
- Pinecone
- Groq
- python-dotenv

## Project Structure

```text
DocuRAG/
│
├── crawler.py
├── processor.py
├── vector_store.py
├── rag.py
├── main.py
├── config.py
├── logger.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### Module Responsibilities

- `crawler.py` — crawls documentation using Tavily.
- `processor.py` — converts crawled content into LangChain Documents and chunks the text.
- `vector_store.py` — configures HuggingFace embeddings, connects to Pinecone, and creates the retriever.
- `rag.py` — builds the retrieval + prompt + LLM generation chain.
- `main.py` — application entry point.

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and configure the required environment variables:

```env
TAVILY_API_KEY=your_tavily_api_key
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
INDEX_NAME=your_pinecone_index_name
```

> Never commit your `.env` file or API keys to GitHub.

## Run

Run the application with:

```bash
python main.py
```

Example question:

```python
query = "What are LangChain agents?"
```

DocuRAG retrieves the most relevant documentation chunks from Pinecone and uses them as context for the LLM.

## Current Features

- Documentation crawling
- LangChain Document conversion
- Text chunking
- HuggingFace embeddings
- Pinecone vector storage
- Semantic similarity retrieval
- Top-k document retrieval
- Context construction
- RAG-based question answering
- Modular Python architecture

## Known Limitations

This is a learning-focused RAG implementation.

Current limitations include:

- Small experimental chunk sizes can produce fragmented retrieval results.
- Retrieval quality has not been optimized.
- No reranking or hybrid search.
- No automated RAG evaluation pipeline.
- Generated answers can still contain claims not fully supported by retrieved context.
- No production API or UI.

## Purpose

DocuRAG was built as a hands-on project to understand the complete RAG pipeline instead of relying only on tutorials.

The project focuses on understanding how crawling, document processing, embeddings, vector databases, retrieval, and LLM generation connect in a modular AI application.