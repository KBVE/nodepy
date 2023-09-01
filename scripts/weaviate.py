import weaviate
from prodict import Prodict
from llama_index.vector_stores import WeaviateVectorStore
from pydantic import BaseModel, Field


import os
import json
import re
import sys


jsonData = Prodict.from_dict(json.loads(sys.argv[1]))

print(f"Done")