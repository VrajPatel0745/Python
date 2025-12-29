# Built-in Data Types
# In programming, data type is an important concept.
#text type: str
x = "Hello World"
print(type(x))
#numeric types: int, float, complex
x = 20
print(type(x))
x = 20.5
print(type(x))
x = 1j
print(type(x))
#sequence types: list, tuple, range
x = ["apple", "banana", "cherry"]
print(type(x))
x = ("apple", "banana", "cherry")
print(type(x))
x = range(6)
print(type(x))
#mapping type: dict
x = {"name" : "John", "age" : 36}
print(type(x))
#set types: set, frozenset
x = {"apple", "banana", "cherry"}
print(type(x))
x = frozenset({"apple", "banana", "cherry"})
print(type(x))
#boolean type: bool
x = True
print(type(x))
#binary types: bytes, bytearray, memoryview
x = b"Hello"
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
print(type(x))
#None type: NoneType
x = None
print(type(x))
# You can get the data type of any object by using the type() function: