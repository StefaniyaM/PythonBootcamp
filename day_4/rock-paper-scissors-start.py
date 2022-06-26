import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]

user_input = int(input("Please choose 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if user_input >=3 or user_input < 0:
  print("You typed an invalid numner.")
else:
  print(game_images[user_input])

computer_numb = random.randint(0, 2)
print("Computer chose: ")

# if user_input == 0:
#   print(rock)
# elif user_input == 1:
#   print(paper)
# elif user_input == 2:
#   print(scissors)
# else:
#   print(None)
 

computer_input = game_images[computer_numb]
print(computer_input)


# if user_input == computer_numb:
#   print("It's a draw.")
# elif user_input == 0 and computer_numb == 1:
#   print("You lose, sorry.")
# elif user_input == 0 and computer_numb == 2:
#   print("You win!")
# elif user_input == 1 and computer_numb == 2:
#   print("You lose, sorry.")
# elif user_input == 1 and computer_numb == 0:
#   print("You win!")
# elif user_input == 2 and computer_numb == 0:
#   print("You lose, sorry.")
# elif user_input == 2 and computer_numb == 1:
#   print("You win!")
# else:
#   print("You type an invalid number")

if user_input > computer_numb:
  print("You win!")
elif user_input == 0 and computer_numb == 2:
  print("You win...")
elif user_input < computer_numb:
  print("You lose...")
elif user_input == 2 and computer_numb == 0:
  print("You lose...")
elif user_input == 0 and computer_numb == 2:
  print("You win!")

