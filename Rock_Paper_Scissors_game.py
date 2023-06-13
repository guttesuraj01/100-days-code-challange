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

#Code is below

import random 

values = [rock, paper, scissors]

user_input = int(input("Select 0 for rock, 1 for paper, 2 for sissors  "))
x = values[user_input]
print(x)
     

computer_variable = random.choice(values)
print('Computer choose',computer_variable)

if user_input == 0 & computer_variable == values[0]:
    print("Draw")
elif input == values[0] & computer_variable == values[1]:
    print("You Loose")
elif input == values[0] & computer_variable == values[2]:
    print("You Won")
# elif input == paper & computer_variable == rock:
#     print("You Won")
# elif input == paper & computer_variable == paper:
#     print("Draw try again")
# elif input == paper & computer_variable == scissors:
#     print("you Won")
else:
    print("Kuch to gadbad hai")

# x = print("Want to try again y/n")

# if x == y or x== Y :
#     print(input)
# elif x== n or X == N:
#     print("Okay")
