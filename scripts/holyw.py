import weaviate
from llama_index.vector_stores import WeaviateVectorStore
from pydantic import BaseModel, Field


import os
import json
import re
import sys


jsonData = json.loads(sys.argv[1])
data = dict(jsonData)

auth_config = weaviate.AuthApiKey(data['weaviate_api'])
client = weaviate.Client( url=data['weaviate_cloud_url'], auth_client_secret=auth_config)


#print(f"{data['$id']}")
print(f"{client.schema.get()}")