# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet ():
  print("Hello everyone.")
  print("This is a training program made by Stefaniya Markova")
  print("By far it is my favourite!")

# greet()

# Function that allows for an input

def greet_with_name(name):
  print(f"Hello {name}!")
  print(f"How are you doing {name}?")

greet_with_name("Steffy")

# Functions with more than one input

def greet_with(name, location):
  print(f"Hello, {name}!")
  print(f"What is it like in {location}?")

greet_with("Steffy", "Majorca")
# greet_with("Majorca", "Steffy") ''' This is called POSITIONAL ARGUEMENT'''

def greet_with(name, location):
  print(f"Hello, {name}!")
  print(f"How is in {location}?")
greet_with(location = "Majorca", name = "Kate")