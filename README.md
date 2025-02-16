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
-[Overview](#overview)
-[Features](#features)
-[Architectures](#architectures)
-[Prerequisties](#prerequisties)
-[Installation](#installation)
-[Configuration](#configuration)

## Overview

The chatbot answers questions by retrieving relevant text fragments from web pages stored in MongoDB Atlas. It uses LangChain chains and agents to integrate LLM-based summarization with a vector-based retrieval mechanism. The project includes functionality to:

-Fetch documents from specified URLs.
-Chunk the documents using a text splitter.
-Generate embeddings using Google Generative AI.
-Store embeddings in a MongoDB Atlas collection configured with a knnVector (vector search) index.
-Answer user queries by retrieving the most relevant chunks and generating a natural language answer.

## Features
-RAG (Retrieval-Augmented Generation): Combines document retrieval with LLM generation to answer questions.
-Document Chunking: Uses `RecursiveCharacterTextSplitter` to break documents into manageable pieces.
-Vector Storage: Embeddings are stored in MongoDB Atlas with a vector search index.

## Prerequisites

- Basic knowledge of Git & Github
- MongoDB
- Python
- Pipenv
- Langchain

## Imp Git commands
    
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
