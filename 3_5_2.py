import json
data = '{"name":"joe", "lastname":"Doe", "age":18}'
data_parsed = json.loads(data)
print(type(data))
print(type(data_parsed))
print(data_parsed['lastname'])
