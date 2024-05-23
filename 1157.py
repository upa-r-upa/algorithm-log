strings=input().upper()
name=dict()

for s in strings:
    name[s] = name.get(s, 0) + 1

max_name = ""
max_value = max(name.values())

for key, value in name.items():
    if max_name != "" and value == max_value:
        max_name = "?"
        break
    elif max_name == "" and value == max_value:
        max_name = key

print(max_name)
