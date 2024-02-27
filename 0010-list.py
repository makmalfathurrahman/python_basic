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
print("fruits[1]   =", fruits[1])
print("fruits[-1]  =", fruits[-1])
print("fruits[1:5] =", fruits[1:5])
print("fruits[:5]  =", fruits[:5])
print("fruits[5:]  =", fruits[5:])

fruits[1] = "ABCD"
print(fruits)
print(len(fruits))

fruits[1:4] = ["ABCD", "EFGH", "IJKL"]
print(fruits)
print(len(fruits))
