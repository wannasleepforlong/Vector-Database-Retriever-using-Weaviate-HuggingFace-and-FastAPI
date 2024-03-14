# Vector Database Retriever using Weaviate, HuggingFace, and FastAPI

This project demonstrates how to build a vector database retriever using Weaviate and the Hugging Face API and deploy it using FastAPI. With this setup, you can store data objects and vector embeddings, enabling efficient retrieval based on similarity measures.

## Introduction

Vector databases have become increasingly popular, especially with the rise of large language models (LLMs). These databases serve as a "long-term memory" for LLMs, allowing them to retrieve information based on similarity rather than exact matches. In this project, we leverage Weaviate, an open-source vector database, along with the Hugging Face API for generating embeddings.

![Project Image](https://github.com/wannasleepforlong/Vector-Database-Retriever-using-Weaviate/assets/109717763/3328d449-ba99-4280-8204-0b02d242e7f3)

This project aims to leverage the open-source Weaviate vector database for vectorizing and querying a small dataframe with the use of Huggingface-tokens and deploy it using FastAPI.

## Features

- **Vectorize Database**: Utilize Weaviate's text2vec module to vectorize textual data for efficient storage and retrieval.
- **Vector Search**: Retrieve the two closest responses from the database based on a given query, utilizing similarity measures.
- **FastAPI Integration**: Integrate Weaviate functionality with a FastAPI application to provide HTTP endpoints for adding data to the database and retrieving results based on user queries.

## Steps to Reproduce

1. Open the command prompt in the project directory.
2. Run 'uvicorn app:app'.
3. Copy the link to your browser (e.g., http://127.0.0.1:8000).
4. Add '/docs' at the end of the link (e.g., http://127.0.0.1:8000/docs).
5. Scroll down to 'Get' and you can change the query and test the program.

![image](https://github.com/wannasleepforlong/Vector-Database-Retriever-using-Weaviate/assets/109717763/b249911a-8c1b-43dd-8f31-348893597607)


## Credits
- Dataset used https://www.kaggle.com/datasets/athu1105/book-genre-prediction
- Thanks to [Leonie](https://medium.com/@iamleonie) for Weaviatte tutorial
