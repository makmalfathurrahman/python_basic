fruits_colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": ["purple", "green"],
    "orange": "orange",
    "melon": "green",
}

print(fruits_colors)
print(len(fruits_colors))
print(fruits_colors["grape"])

print("----------")


# Create New Dictionaries
fruits_colors["STARFRUIT"] = ["yellow", "green"]
print(fruits_colors)

print("----------")


# Create New Dictionaries
new_dict = dict(
    brand="Toyota",
    electric=False,
    year=2024,
    colors=["red", "white", "blue"],
)
print(new_dict)
print(len(new_dict))
