import json

with open("C:/Users/nuc/project/CSE_Chat_Project/data/Free_recent.json", 'r', encoding="UTF-8") as file:
    data = json.load(file)
    print(type(data))
    print(data)