fruits = (
    "apple",
    "banana",
    "orange",
    "grape",
    "strawberry",
)

print(fruits)
print(len(fruits))

print("----------")


# Unpack
(
    apple,
    banana,
    orange,
    grape,
    strawberry,
) = fruits
print(apple)
print(banana)
print(orange)
print(grape)
print(strawberry)

print("----------")


# Unpack Using Asterisk *
(
    apple,
    banana,
    *rest_fruit,
) = fruits
print(apple)
print(banana)
print(rest_fruit)

print("----------")

(
    apple,
    *rest_fruit,
    grape,
    strawberry,
) = fruits
print(apple)
print(rest_fruit)
print(grape)
print(strawberry)

print("----------")
