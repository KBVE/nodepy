import sys
import json

data = sys.argv[1]
jsonData = json.loads(data)

if jsonData['bigman']:
    name = jsonData['bigman']
    print(f"Hello, {name} how are you?")