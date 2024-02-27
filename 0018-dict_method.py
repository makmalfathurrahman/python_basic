car_spec = {
    "brand": "Toyota",
    "electric": False,
    "year": 2024,
    "colors": ["red", "white", "blue"],
}

print(car_spec)
print(len(car_spec))

print("----------")


# Get
data = car_spec.get("colors")
print(data)
print(len(data))

print("----------")


# Keys
data = car_spec.keys()
print(data)
print(len(data))


print("----------")


# Keys
data = car_spec.values()
print(data)
print(len(data))


print("----------")


# Items
data = car_spec.items()
print(data)
print(len(data))


print("----------")


# Update
car_spec.update({"brand": "Lamborghini"})
print(car_spec)
print(len(data))

print("----------")


# Add Using Update
car_spec.update({"tires": 4})
print(car_spec)
print(len(data))

print("----------")


# Pop
car_spec.pop("year")
print(car_spec)
print(len(data))

print("----------")


# Popitem
car_spec.popitem()
print(car_spec)
print(len(data))

print("----------")


# Clear
car_spec.clear()
print(car_spec)
print(len(data))
