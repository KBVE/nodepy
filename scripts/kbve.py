import sys
import json
import os

from pocketbase import PocketBase  # Client also works the same
from pocketbase.client import FileUpload

def data():
    data = sys.argv[1]
    if data is None:
        print("No Data Received, provide data query parameter with json")
        exit()
    try:
        jsonData = json.loads(data)
    except ValueError as e:
        print(f"Error when loading json: {e}. Please provide data query parameter with json")
        exit()
    else:
        pass
    return jsonData

def getter( key ):
    getData = data()
    getKey = None
    
    if f"{key}" in getData:
        getKey = getData[f"{key}"]

    if getKey is None:
        print("Failed to find f{key}")
        exit()

    return getKey
