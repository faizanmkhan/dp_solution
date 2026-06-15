import json

data = input()
d = json.loads(data)

new_dict = {}

for key, value in d.items():
    if value is not None:
        new_dict[key] = value

print(new_dict)