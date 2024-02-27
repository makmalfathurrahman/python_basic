fruits = {
    "apple",
    "banana",
    "orange",
    True,
    "strawberry",
    5,
}

print(fruits)
print(len(fruits))

print("----------")


# Add
fruits.add(False)

print(fruits)
print(len(fruits))

print("----------")


# Update
fruits_update = {
    "CHERRY",
    "MelOn",
    1000,
}

fruits_update_list = [
    -75,
    "P L U M",
]


fruits.update(fruits_update)
print(fruits)
print(len(fruits))

print("----------")

fruits.update(fruits_update_list)
print(fruits)
print(len(fruits))

print("----------")


# Remove
fruits.remove(5)
print(fruits)
print(len(fruits))

print("----------")


# Discard
fruits.discard("orange")
print(fruits)
print(len(fruits))

print("----------")


# Clear
fruits.clear()
print(fruits)
print(len(fruits))

print("----------")
