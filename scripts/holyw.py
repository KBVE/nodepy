import weaviate
from prodict import Prodict
from llama_index.vector_stores import WeaviateVectorStore
from pydantic import BaseModel, Field


import os
import json
import re
import sys


jsonData = Prodict.from_dict(json.loads(sys.argv[1]))

auth_config = weaviate.AuthApiKey(jsonData.data.weaviate_api)
client = weaviate.Client(
    url=jsonData.data.weaviate_cloud_url,
    auth_client_secret=auth_config
)


print(f"Done")