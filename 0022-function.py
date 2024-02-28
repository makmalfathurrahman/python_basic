def function():
    print("This is from function")


function()

print("----------")


# Function Parameter
def function(string1, string2):
    print(string1 + string2)


function("Hello ", "World!")

print("----------")


# Function Default Parameter
def function(country="Indonesia"):
    print(country)


function("Saudi Arabia")
function()
function("Turkey")

print("----------")


# Function Return Value
def function(string):
    return string


print(function("Hello World!"))

print("----------")
