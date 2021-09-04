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

import random

data = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(data[choice])
print("Computer chose:")

computer_choice = random.randint(0,2)
print(data[computer_choice])

if choice == 0:
  if computer_choice == 0:
    print("Draw.")
  elif computer_choice == 1:
    print("You Lose.")
  else:
    print("You Win.")
elif choice == 1:
  if computer_choice == 0:
    print("You Win.")
  elif computer_choice == 1:
    print("Draw.")
  else:
    print("You Lose.")
elif choice == 2:
  if computer_choice == 0:
    print("You Lose.")
  elif computer_choice == 1:
    print("You Win.")
  else:
    print("Draw.")