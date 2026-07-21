# 🍕 Local Pizza Restaurant RAG Agent

A fully local Retrieval-Augmented Generation (RAG) system built with **LangChain**, **ChromaDB**, and **Ollama**. This application embeds customer reviews from a CSV dataset into a local vector database and uses an LLM to answer user questions based on authentic context.

---

## 🛠️ Features

* **100% Local Execution**: Runs entirely on your local machine using Ollama (no API keys required).
* **Vector Search**: Uses `mxbai-embed-large` embeddings via ChromaDB to find relevant restaurant reviews.
* **Smart RAG Pipeline**: Combines retrieved review context with `llama3.2` to generate accurate, context-aware answers.
* **Persistent Storage**: Converts and embeds data only on the first run for fast subsequent query performance.

---

## 📂 Project Structure

```text
local-ai-agent/
│
├── main.py                          # Terminal interface & RAG query loop
├── vector.py                        # CSV loading, embeddings, and ChromaDB setup
├── realistic_restaurant_reviews.csv # Dataset containing customer reviews
├── requirements.txt                 # Python dependencies
└── .gitignore                       # Git exclusion rules
