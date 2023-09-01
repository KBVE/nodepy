import weaviate
from llama_index.vector_stores import WeaviateVectorStore
from pydantic import BaseModel, Field


import os
import json
import re
import sys


data = sys.argv[1]
jsonData = json.loads(data)
print(f"{jsonData}")
