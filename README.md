# Chatbot Demo with RAG 

You need to install the following Python Packages to in the Python environment of this
project:

## Python
pip install -U pip

pip install streamlit

pip install psycopg2-binary

pip install langchain

pip install langchain-community

pip install sentence-transformers

pip install langchain-ollama

pip install pydef

## Ollama
To run Ollama locally in your machine you need to install it. Follow instructions here:

https://ollama.com/

Once installed, you need to pull Llama3.2 (3B parameter version) to download it with the
following command:

ollama pull llama3.2

At this point you have the Llama3.2 running locally

## PG Vector
You need install and enable pgvector to create columns with vector. In heroku is already
installed, buy you need to enable it in your database.

Here are the instructions:

https://dev.to/farez/installing-postgresql-pgvector-on-debian-fcf

Adapt to your version of postgresql. Mine is version 17.

## Schema
Folder sql has a file named schema.sql with the commands to create the tables

## Script example.py
This script show how the embeddings work. It is run with the following command:

python example.py

## Script filehandler.py
This script read pdf files in the directory named files, converts them to text, splits
the text in chunks, and then tokenizes the chunk in two passes. The first pass uses a
RecursiveCharacterTextSplitter to split the text in chunks. The second pass uses a
SentenceTransformersTokenTextSplitter to tokenize the text. Finally, the chunks have
embedding computed, and inserted into the postgres database. The database and tables
must be created before running this script.

You need to run this script only once as follows:

python filehandler.py

## Chatbot
The chabot is run as a Streamlit app. It used the ChatOllamaBot class to implement the
LLM calls, creating a prompt and adding context by using Retrieval Augmented Generation
(RAG) to bring data from postgres.

The chatbot is run as follows:

streamlit run chatbot.py



