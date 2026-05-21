# =========================================
# Intelligent Document Intelligence Platform
# =========================================

import PyPDF2
import faiss
import re
import numpy as np
from openai import OpenAI


# =========================================
# OpenAI API Configuration
# =========================================

raw = open("openai_key.py", "r").read()

m = re.search(r"(sk-[A-Za-z0-9\-_]+)", raw)

if not m:
    raise RuntimeError("No API key found")

api_key = m.group(1)

client = OpenAI(api_key=api_key)


# =========================================
# Read PDF
# =========================================

def read_pdf(path):

    reader = PyPDF2.PdfReader(path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


# =========================================
# Create Chunks
# =========================================

def make_chunks(text, chunk_size=700):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start = end

    return chunks


# =========================================
# Generate Embeddings
# =========================================

def get_embeddings(chunkslist):

    embeddings = []

    for chunk in chunkslist:

        response = client.embeddings.create(
            input=chunk,
            model="text-embedding-3-small"
        )

        vector = response.data[0].embedding

        embeddings.append(vector)

    return np.array(embeddings).astype("float32")


# =========================================
# Build FAISS Index
# =========================================

def build_faiss_index(embeddings):

    dimension = len(embeddings[0])

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index


# =========================================
# Search Relevant Chunks
# =========================================

def search_chunks(question, chunks, index):

    q_embed = client.embeddings.create(
        input=question,
        model="text-embedding-3-small"
    ).data[0].embedding

    q_embed = np.array([q_embed]).astype("float32")

    distances, indices = index.search(q_embed, k=3)

    best_chunks = [chunks[i] for i in indices[0]]

    return best_chunks


# =========================================
# Ask GPT Model
# =========================================

def ask_question(chunks, question):

    context = "\n\n".join(chunks)

    prompt = f"""
You are an intelligent enterprise document assistant.

Answer the question ONLY from the provided context.

If the answer is not present in the context,
reply with:

'Information not available in uploaded document.'

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a highly intelligent AI assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# =========================================
# Main Pipeline
# =========================================

def main(uploaded_file, question):

    text = read_pdf(uploaded_file)

    chunks = make_chunks(text)

    embeddings = get_embeddings(chunks)

    embeddings = np.array(embeddings).astype("float32")

    index = build_faiss_index(embeddings)

    best_chunks = search_chunks(question, chunks, index)

    answer = ask_question(best_chunks, question)

    return answer
