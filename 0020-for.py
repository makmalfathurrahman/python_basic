# For In
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

print("----------")


# For In String
for i in "mango":
    print(i)

print("----------")


# For In Range
for i in range(6):
    print(i)

print("----------")

for i in range(2, 6):
    print(i)

print("----------")

for i in range(1, 10, 2):
    print(i)

print("----------")

for i in range(6):
    print(i)
else:
    print("Finish!")

print("----------")


# Break Statement
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i == "banana":
        break
    print(i)

print("----------")


# Continue Statement
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i == "banana":
        continue
    print(i)

print("----------")
