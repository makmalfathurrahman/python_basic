fruits = (
    "apple",
    "banana",
    "orange",
    "kiwi",
    "grape",
    "pineapple",
    "strawberry",
    "blueberry",
    "pear",
)

print(fruits)
print(len(fruits))

print("----------")


fruits_to_list = list(fruits)
fruits_to_list[0] = "APPLE"
fruits = tuple(fruits_to_list)
print(fruits)
print(len(fruits))

print("----------")


# Append - Method 1
fruits_to_list = list(fruits)
fruits_to_list.append("PAPAYA")
fruits = tuple(fruits_to_list)
print(fruits)
print(len(fruits))

print("----------")


# Add - Method 2
add_fruits = (
    "DRAGON FRUIT",
    "MANGO",
)
fruits += add_fruits
print(fruits)
print(len(fruits))

print("----------")


# Delete by Index
delete_fruits = list(fruits)
delete_fruits.remove("banana")
fruits = tuple(delete_fruits)
print(fruits)
print(len(fruits))

print("----------")


# Delete
clear_fruits = list(fruits)
clear_fruits.clear()
fruits = tuple(clear_fruits)
print(fruits)
print(len(fruits))

print("----------")
