import sys
import json

data = sys.argv[1]
jsonData = json.loads(data)
print(jsonData)