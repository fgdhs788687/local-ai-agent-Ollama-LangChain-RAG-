import os
import pandas as pd
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings

# Reading the csv file:
df = pd.read_csv("realistic_restaurant_reviews.csv")

# Embeddings model:
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"

# Check if the database file actually exists inside the directory
db_exists = os.path.exists(os.path.join(db_location, "chroma.sqlite3"))

vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings,
)

# Only process and add documents if the DB hasn't been created yet
if not db_exists:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content=f"{row['Title']} {row['Review']}",
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id=str(i),
        )
        ids.append(str(i))
        documents.append(document)

    vector_store.add_documents(documents=documents, ids=ids)

# Retriever setup
retriever = vector_store.as_retriever(search_kwargs={"k": 5})