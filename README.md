# RAG Chatbot

This project is a Retrieval-Augmented Generation (RAG) chatbot built with LangChain, Google Generative AI, and MongoDB Atlas. It loads documents from specified URLs, chunks the text, generates embeddings, stores them in a MongoDB Atlas vector search collection, and then uses a retrieval chain (via LangChain) to answer user queries.

> **Warning:** 
> 
> Please do not expose sensitive information such as passwords, API keys, or any other confidential data in your code. 
> 
> Always use environment variables or secure vaults to manage sensitive information. 
> 
> Exposing such data can lead to security vulnerabilities and unauthorized access to your systems.

## Table of Contents
- [Overview](#overview) 
- [Features](#features) 
- [Architectures](#architectures) 
- [Prerequisties](#prerequisties)
- [Installation](#installation)
- [Configuration](#configuration)
- [License](#license)

## Overview

The chatbot answers questions by retrieving relevant text fragments from web pages stored in MongoDB Atlas. It uses LangChain chains and agents to integrate LLM-based summarization with a vector-based retrieval mechanism. The project includes functionality to:

- Fetch documents from specified URLs. 
- Chunk the documents using a text splitter. 
- Generate embeddings using Google Generative AI. 
- Store embeddings in a MongoDB Atlas collection configured with a knnVector (vector search) index. 
- Answer user queries by retrieving the most relevant chunks and generating a natural language answer. 

## Features

- RAG (Retrieval-Augmented Generation): Combines document retrieval with LLM generation to answer questions.
- Document Chunking: Uses `RecursiveCharacterTextSplitter` to break documents into manageable pieces.
- Vector Storage: Embeddings are stored in MongoDB Atlas with a vector search index.

## Architecture
- Document Loading & Processing: The Vectorize class (in `vector.py`) downloads documents from a list of URLs, splits the text into chunks, and generates embeddings.
- Embedding Storage: Generated embeddings are stored in a MongoDB Atlas collection. A vector search index is created on the embedding field.
Query Handling: The Bot class (in `query.py`) sets up a retrieval chain using LangChain. When a user inputs a query, the retrieval chain searches MongoDB for the most similar document chunks and passes them as context to the LLM.
- Response Generation: The LLM (Google Generative AI via LangChain) generates the final answer based solely on the retrieved context.

## Prerequisites

- Basic knowledge of Git & Github
- MongoDB
- Python
- Pipenv
- Langchain
 
## Installation

### Clone the Repository
```sh
git clone https://github.com/beBijayeeni/marvel-mongo.git
```

## Imp Pipenv commands
- **Install pipenv package**:

    ```bash
    pip install pipenv
    ```


- **Initialize a virtual environment**:

    ```bash
    pipenv install
    ```

- **Start the pipenv terminal**:

    ```bash
    pipenv shell
    ```
- **Install required in your venv**:

    ```bash
    pipenv install -r requirements.txt
    ```

## Configuration

### Environment Variables
Create a `.env` file in the project root with the following (adjust values as needed):
```bash
# Google Generative AI API key
GEMINI_API_KEY=your_google_gemini_api_key

# MongoDB Atlas connection string and database info
ATLAS_CONNECTION_STRING=your_mongodb_atlas_connection_string
DB_NAME=your_database_name
COLLECTION_NAME=your_collection_name
VECTOR_INDEX=your_vector_index_name

# (Optional) Custom user agent for HTTP requests
USER_AGENT=LLM_APP_DEMO/1.0
```

### MongoDB Atlas Setup
- Cluster and Database: Log into MongoDB Atlas and create a new cluster if you don’t have one. Create (or use an existing) database that matches `DB_NAME`.

- Collection: Create a collection with the name in `COLLECTION_NAME`. This is where your embeddings and documents will be stored.

- Vector Search Index: In your collection’s “Search” tab, create a custom index using a definition similar to:
```bash
{
  "mappings": {
    "dynamic": true,
    "fields": {
      "embedding": {
        "type": "knnVector",
        "dimensions": 768,
        "similarity": "cosine"
      }
    }
  }
}
```
Save the index; it may take a few minutes to build.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
