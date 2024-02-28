import json

data = '{"name":"Melon", "color":"Green"}'

result = json.loads(data)
print(result)

print("----------")


# Convert to JSON
fruits = {
    "apple": "red",
    "banana": "yellow",
    "grape": ["purple", "green"],
    "orange": "orange",
    "melon": "green",
}

result = json.dumps(fruits)
print(result)

print("----------")


# Convert Python Data Type to JSON
print(json.dumps({"name": "Melon", "color": "Green"}))
print(json.dumps([1, 2]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("Hello World!"))
print(json.dumps(10))
print(json.dumps(7.5))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("----------")
