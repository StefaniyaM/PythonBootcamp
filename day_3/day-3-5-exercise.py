# 🚨 Don't change the code below 👇

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name3 = name1 + " " + name2
name3_lower = name3.lower()

t_letter = name3_lower.count("t")
r_letter = name3_lower.count("r")
u_letter = name3_lower.count("u")
e_letter = name3_lower.count("e")

total1 = t_letter + r_letter + u_letter + e_letter

l_letter = name3_lower.count("l")
o_letter = name3_lower.count("o")
v_letter = name3_lower.count("v")
e_letter = name3_lower.count("e")

total2 = l_letter + o_letter + v_letter + e_letter

total = str(total1) + str(total2)
# print(total)

total_score = int(total)

if total_score < 10 or total_score > 90:
  print(f"Your score is {total_score}, you go like coke and menton")
elif 40 <= total_score <= 50:
 
  print(f"Your score is {total_score}, you are alright together")
else:
  print(f"Your score is {total_score}.")