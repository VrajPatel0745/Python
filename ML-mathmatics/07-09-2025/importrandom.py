import random
# Import the random module, and display a random number between 1 and 9:
# randint() method returns a random integer between the two specified numbers (including both)
# randrange() method returns a randomly selected element from the specified range
print(random.randint(1, 9))
print(random.randrange(1, 10))
# choice() method returns a randomly selected element from the specified sequence
print(random.choice(['apple', 'banana', 'cherry']))
# random() method returns a random float number between 0.0 and 1.0
print(random.random())
# uniform() method returns a random float number between the two specified numbers
print(random.uniform(1.0, 10.0))
# sample() method returns a list with a randomly selection of items from the specified sequence
print(random.sample(['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango'], 3))
