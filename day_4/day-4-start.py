import random

random_integer = random.randint(1, 10)
print(random_integer)

# 0.000000.... to 0.9999999....
random_float = random.random()
print(random_float)

randomFloat = random_float * 5
print(randomFloat)

# Love calculator from previous task is based on random letters in the names
# Therefore we can use random score system to show us results from 1 - 100

love_score = random.randint(1, 100)
print(f"Your Love score is {love_score}.")


# ==============================


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina","New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tenessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma","New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[-50])
print(states_of_america[6])
states_of_america[6] = "Merriedland"
# print(states_of_america)

states_of_america.append("Kewinland")
# print(states_of_america)




