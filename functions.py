def new_function():
    print("well done jiya, you are amazing, love you my babygirl")


new_function()

# with arguments

def game_generator(game):
    # ADD A COLON AT THE END
    print("The game is " + game)

game_generator("COD")

# WITH 2 ARGUMENTS
def greeting_name(fname, lname):
  print("Hello " + fname + " "+ lname)

greeting_name("Jiya", "Bharti")


# Arbitrary arguments
# If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def greeting_names(*names):
    print("Hello introducing " + names[3])

my_function("lisa", "Sofia", "alia")


# keyword arguments
def kids_function(child3, child2, child1):
  print("The youngest child is " + child3)

kids_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# dont see a point of this!

# DEFAULT PARAMETER
def country_function(country ="Norway"):
  #   if i dont put in a argument norway comes up, if i do then the argument comes up
  print("I am from " + country)

country_function("Sweden")
country_function("India")
country_function()
country_function("Brazil")

# PASSING A LIST INTO AN ARGUMENT

def FOOD_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
Burgers = ["hamburger", "cheeseburger", "mclegend"]
FOOD_function(fruits)
FOOD_function(Burgers)


def numbers_function(numbers):
    for x in numbers:
        return str

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers_function(numbers)



def filter_list():
    for str in list:
        print(str)


list = [1,2, "hi", 3, "yo"]
filter_list()


# RETURN VALUES

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

