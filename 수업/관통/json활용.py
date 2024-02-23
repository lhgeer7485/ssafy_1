import json

json_data = '''{"name" : "kim", "age" : 28}'''

data = json.loads(json_data)

print(data['name'])
