import json

sample_data_01 = { "name": "John", "lastname": "Doe", "age": 24}
sample_data_01_json = json.dumps(sample_data_01)
print(type(sample_data_01_json))
print(sample_data_01_json)
