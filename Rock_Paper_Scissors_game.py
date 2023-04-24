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

random_values = [rock, paper, scissors]
input = input('choose on out of rock / paper / siccors')
print(input)
computer_variable = random.choice(random_values)
print('Computer choose',computer_variable)

# if input == rock & computer_variable == rock:
#     print('Draw Try Again', input)
# elif input == rock & computer_variable == paper:
#     print("You Loose")
# elif input == rock & computer_variable == scissors:
#     print("You Won")
# elif input == paper & computer_variable == rock:
#     print("You Won")
# elif input == paper & computer_variable == paper:
#     print("Draw try again")
# elif input == paper & computer_variable == scissors:
#     print("you Won")
# else:
#     print("Kuch to gadbad hai")

# x = print("Want to try again y/n")

# if x == y or x== Y :
#     print(input)
# elif x== n or X == N:
#     print("Okay")
