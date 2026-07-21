# 🍕 Local Pizza Restaurant RAG Agent

A fully local Retrieval-Augmented Generation (RAG) system built with **LangChain**, **ChromaDB**, and **Ollama**. This application embeds customer reviews from a CSV dataset into a local vector database and uses a local LLM to answer user questions accurately based on relevant context.

---

## 🛠️ Features

* **100% Local & Private**: Runs entirely on your local machine using Ollama with no API keys or cloud services required.
* **Vector Search**: Uses `mxbai-embed-large` embeddings stored in ChromaDB to retrieve the most relevant reviews.
* **Context-Aware Responses**: Connects retrieved context to `llama3.2` to generate accurate answers based strictly on real customer feedback.
* **Persistent Storage**: Converts and embeds data into ChromaDB on the first run so subsequent queries run fast without re-embedding.

---

## 📂 Project Structure

* `main.py`: CLI interface and RAG query execution loop.
* `vector.py`: CSV parsing, embedding generation, and ChromaDB vector store setup.
* `realistic_restaurant_reviews.csv`: Restaurant review dataset.
* `requirements.txt`: Core Python dependencies.
* `.gitignore`: Rules for ignoring local databases, virtual environments, and caches.
* `README.md`: Project documentation.

---

## 📋 Prerequisites

1. **Python 3.10+**
2. **Ollama**: Download and install from [ollama.com](https://ollama.com).

Before running the project, pull the required local models in your terminal:

```powershell
# Pull the embedding model
ollama pull mxbai-embed-large

# Pull the LLM model
ollama pull llama3.2

```

---

## 🚀 Getting Started

### 1. Clone the Repository

```powershell
git clone https://github.com/YOUR_USERNAME/local-ai-agent.git
cd local-ai-agent

```

### 2. Set Up a Virtual Environment

```powershell
# Create virtual environment
python -m venv venv

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activate on Mac/Linux
source venv/bin/activate

```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt

```

### 4. Ensure Ollama Service is Running

Make sure the Ollama desktop application is active in your system tray, or start it manually in a separate terminal window:

```powershell
ollama serve

```

### 5. Run the Application

```powershell
python main.py

```

---

## 💬 Example Usage

```text
ask your question (q or Q to quit): What do people say about the crust?

Based on the reviews provided, customers consistently praise the crust! 
Multiple reviewers mention that it has a perfectly crispy exterior while remaining 
soft and chewy on the inside...

```

---

## ⚙️ How It Works

1. **Data Ingestion (`vector.py`)**: Reads `realistic_restaurant_reviews.csv` using Pandas and formats each review into a LangChain `Document`.
2. **Embedding & Storage**: Converts text into vector embeddings using `mxbai-embed-large` and saves them locally in `./chroma_langchain_db`.
3. **Retrieval (`main.py`)**: Searches ChromaDB for the top 5 most relevant reviews matching your prompt (`k=5`).
4. **Generation**: Constructs a prompt containing the retrieved reviews and uses `llama3.2` to generate a tailored answer.
