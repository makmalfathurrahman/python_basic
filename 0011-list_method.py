fruits = [
    "apple",
    "banana",
    "orange",
    "kiwi",
    "grape",
    "pineapple",
    "strawberry",
    "blueberry",
    "pear",
]

print(fruits)
print(len(fruits))

print("----------")


# Insert
fruits.insert(2, "WATERMELON")
print(fruits)
print(len(fruits))

print("----------")


# Append
fruits.append("DRAGON FRUIT")
print(fruits)
print(len(fruits))

print("----------")


# Extend
fruits_extend = ["mango", "papaya", "melon"]
fruits.extend(fruits_extend)
print(fruits)
print(len(fruits))

print("----------")


# Extend
fruits_extend = ["mango", "papaya", "melon"]
fruits.extend(fruits_extend)
print(fruits)
print(len(fruits))

print("----------")


# Remove
fruits.remove("apple")
print(fruits)
print(len(fruits))

print("----------")


# Remove by Index
fruits.pop(0)
print(fruits)
print(len(fruits))

print("----------")


# Clear
fruits.clear()
print(fruits)
print(len(fruits))

print("----------")
