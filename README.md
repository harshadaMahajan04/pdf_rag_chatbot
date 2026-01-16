# PDF RAG Chatbot

A local PDF-based RAG (Retrieval-Augmented Generation) chatbot built with **FastAPI**, **Hugging Face Transformers**, and a **vector store** using **Sentence Transformers**.  
It can answer questions, summarize, and explain content from uploaded PDFs.

---

## Features

- Upload PDF documents via API
- Automatically extract and chunk text
- Build embeddings for efficient retrieval
- Use local LLM (Hugging Face summarization models) for generating answers
- Returns coherent summaries and explanations for user queries
- Fully local – no OpenAI API required

---

## Tech Stack

- **Backend:** FastAPI  
- **Embeddings:** sentence-transformers (`all-MiniLM-L6-v2`)  
- **Vector Store:** sklearn NearestNeighbors + NumPy  
- **LLM / Summarization:** Hugging Face Transformers (`facebook/bart-large-cnn`)  
- **Frontend:** Optional React app (CORS enabled)

---

## Installation

```bash
# 1. Clone the repo
git clone https://github.com/<USERNAME>/<REPO>.git
cd <REPO>

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # mac/linux
venv\Scripts\activate     # windows

# 3. Install dependencies
pip install -r requirements.txt




Usage

Run the FastAPI backend:

uvicorn main:app --reload


Upload a PDF:

POST http://127.0.0.1:8000/upload-doc
Form data: file=<your pdf>


Ask questions:

POST http://127.0.0.1:8000/ask
JSON body: {"question": "Give the summary of the PDF"}


The response will return a summarized answer generated from the PDF content.

Project Structure
pdf-rag-chatbot/
│
├─ main.py              # FastAPI backend
├─ vector_store.py      # Embeddings + vector DB
├─ rag.py               # Generate answer logic
├─ utils.py             # PDF extraction and chunking
├─ requirements.txt     # Python dependencies
└─ README.md

Requirements
fastapi
uvicorn
pydantic
sentence-transformers
scikit-learn
numpy
transformers
PyPDF2