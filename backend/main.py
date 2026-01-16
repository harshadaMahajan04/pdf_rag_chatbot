from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils import extract_text_from_pdf, chunk_text
from vector_store import add_chunks_to_vector_db, search_similar_chunks
import os

app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str

@app.post("/upload-doc")
async def upload_doc(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)
    chunks = chunk_text(text)
    add_chunks_to_vector_db(chunks)

    os.remove(file_path)

    return {"message": "PDF uploaded successfully"}

@app.post("/ask")
async def ask_question(req: QuestionRequest):
    chunks = search_similar_chunks(req.question, k=3)

    if not chunks:
        return {"answer": "I don't know. Please upload a document first."}

    return {"answer": " ".join(chunks)}




