# Text Data Type
string = "Hello World"
print("string =", type(string))

print("----------")


# Numeric Data Type
integer = 10
float = 7.5
complex = 10j
print("integer =", type(integer))
print("float =", type(float))
print("complex =", type(complex))

print("----------")


# Sequence Data Type
list = [1, 2, 3, 4, 5]
tuple = ("one", "two", "three")
range = range(10)
print("list =", type(list))
print("tuple =", type(tuple))
print("range =", type(range))

print("----------")


# Mapping Data Type
mapping = {"Name": "Alex", "Age": 20}
print("mapping =", type(mapping))

print("----------")


# Set Data Type
set = {"four", "five", "six"}
frozenset = frozenset({"four", "five", "six"})
print("set =", type(set))
print("frozenset =", type(frozenset))

print("----------")


# Boolean Data Type
boolean = True
print("boolean =", type(boolean))

print("----------")


# Binary Data Type
bytes_ = b"Hello"
bytearray = bytearray(10)
memoryview = memoryview(bytes(10))
print("bytes =", type(bytes_))
print("bytearray =", type(bytearray))
print("memoryview =", type(memoryview))

print("----------")


# None Data Type
x = None
print("x =", type(x))
