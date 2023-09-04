# Lian Li Script - Will delete after some general test casing

# Weaviate
import weaviate

# Llama Index
from llama_index.vector_stores import WeaviateVectorStore

# Pydantic
from pydantic import BaseModel, Field


# Unstructured
from unstructured.documents.elements import Text, ListItem, NarrativeText, Title, Element
from unstructured.documents.html import HTMLDocument
# [1] Will the Docker container need additional files within the base ubuntu image to use the auto?
# from unstructured.partition.auto import partition



# Internals

import os
import json
import re
import sys

# JSON
jsonData = json.loads(sys.argv[1])
data = dict(jsonData)


# Weaviate - [START]

auth_config = weaviate.AuthApiKey(data['weaviate_api'])
client = weaviate.Client( url=data['weaviate_cloud_url'], auth_client_secret=auth_config)


# Weaviate - [END]



# FINAL
#print(f"{data['$id']}")
print(f"{client.schema.get()}")