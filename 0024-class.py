class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self) -> str:
        return f"Hello {self.name}"

    def call_fruit(self):
        print(self.name, "with", self.color, "color")

    banana = "Banana"


fruit = Fruits("Strawberry", "Red")
print(fruit)
print("name  =", fruit.name)
print("color =", fruit.color)
fruit.call_fruit()
print(fruit.banana)

print("----------")
