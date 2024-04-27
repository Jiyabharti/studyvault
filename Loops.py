
"""For Loops"""

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# print each fruit in the fruit list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#   even strings are iterable objects
for x in "banana":
  print(x)


"""break statements"""
# With the break statement we can stop the loop before it has looped through all the items:





"""Nested Loops"""

# = a loop within another loop
#                       outer loop:
#                           inner loop:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]


# this means for the value in adjective
for x in adj:
  for y in fruits:
    print(x, y)