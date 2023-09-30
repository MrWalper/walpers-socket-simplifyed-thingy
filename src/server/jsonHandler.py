import json

def getJson(path:str):
    with open(path,"r") as file:
        data = json.load(file)
        return data