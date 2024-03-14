import weaviate
from fastapi import FastAPI
import pandas as pd
import json
from weaviate.util import generate_uuid5

app = FastAPI()

auth_config = weaviate.AuthApiKey(api_key="qlSLo66aoYuIBHkdfH0Vn2dNP2yrruXOY4Cv")  # Weaviate instance API key
# Instantiate the client
client = weaviate.Client(
    url="https://cluster-db-9rtfspng.weaviate.network", # Weaviate cluster URL
    auth_client_secret=auth_config,
    additional_headers={
        "X-HuggingFace-Api-Key": "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", # API key
        }
)
df = pd.read_csv("data.csv", nrows = 100)
df = df.head(5)

class_obj = {
    # Class definition
    "class": "BookQuest",

    # Property definitions
    "properties": [
        {
            "name": "title",
            "dataType": ["text"],
        },
        {
            "name": "genre",
            "dataType": ["text"],
        },
        {
            "name": "summary",
            "dataType": ["text"],
        },
    ],

      # Specify a vectorizer
    "vectorizer": "text2vec-huggingface",

    # Module settings
    "moduleConfig": {
         "text2vec-huggingface": {
          "model": "sentence-transformers/all-MiniLM-L6-v2",
          "options": {
            "waitForModel": True,
            "useCache": True
          }
        },
        "qna-huggingface": {  # Question answering module configuration
            "model": "distilbert-base-uncased-distilled-squad (uncased)"  # question answering model
        }
    }
}

try:
    client.schema.create_class(class_obj)
    print("Class 'BookQuest' created successfully.")
except weaviate.exceptions.UnexpectedStatusCodeError as e:
    # Check if the error is due to the class already existing
    if e.status_code == 422 and 'class name "BookQuest" already exists' in str(e):
        print("Class 'BookQuest' already exists. Skipping creation.")


# Endpoint to add data to Weaviate
@app.post("/add_data")
def add_data():
    with client.batch.configure(batch_size=10, num_workers=1) as batch:
        for _, row in df.iterrows():
            question_object = {
                "title": row.title,
                "genre": row.genre,
                "summary": row.summary
            }
            batch.add_data_object(
                question_object,
                class_name="BookQuest",
                uuid=generate_uuid5(question_object)
            )
    return {"message": "Data added to Weaviate successfully"}

# Endpoint to get results based on concept
@app.get("/get_results/{concept}")
def get_results(concept: str):
    res = client.query.get("BookQuest", ["title", "genre", "summary"]) \
        .with_near_text({"concepts": concept}) \
        .with_limit(2) \
        .do()
    return {"results": res}

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
