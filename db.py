import weaviate
import requests
import json
from weaviate.classes.config import Configure
import os
from dotenv import load_dotenv


client = weaviate.connect_to_local()

print(client.is_ready())

try:
    # CREATE COLLECTION
    # questions = client.collections.create(
    #     name="Question",
    #     vectorizer_config=[
    #         Configure.NamedVectors.text2vec_ollama(
    #             name="title_vector",
    #             source_properties=["question", "answer"],
    #            api_endpoint=os.getenv("VECTORIZER_API_ENDPOINT"),
    #             model="nomic-embed-text",
    #         )
    #     ],
    #     generative_config=Configure.Generative.ollama(
    #         api_endpoint=os.getenv("GENERATIVE_API_ENDPOINT"),
    #         model="tinyllama",
    #     ),
    # )

    # ADD DATA
    # resp = requests.get(
    #     "https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json"
    # )
    # data = json.loads(resp.text)  # Load data
    # 
    # question_objs = list()
    # for i, d in enumerate(data):
    #     question_objs.append(
    #         {
    #             "answer": d["Answer"],
    #             "question": d["Question"],
    #             "category": d["Category"],
    #         }
    #     )
    # 
    # questions = client.collections.get("Question")
    # questions.data.insert_many(question_objs)

    # QUERIES
    print("SEMANTIC:")
    questions = client.collections.get("Question")

    response = questions.query.near_text(query="biology", limit=2)

    print(response.objects[0].properties)  # Inspect the first object

    print("\n\nGENERATIVE:")

    response = questions.generate.near_text(
        query="biology",
        limit=2,
        single_prompt="explain question {question}",
    )

    print(response.objects[0].generated)  # Inspect the generated text

except Exception as e:
    raise e
finally:
    client.close()
