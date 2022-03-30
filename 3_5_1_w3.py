import json

sample_data_02 = {
  "name": "John",
  "age": 24,
  "married": True,
  "divorced": False,
  "children": ("Bruce"),
  "cars": [
    {"model": "corolla", "year": 2020},
  ]
}

print(json.dumps(sample_data_02))
print(json.dumps(sample_data_02, indent=4))
