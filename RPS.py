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

import random

h = input('Input please')

# if h != r or h != p or h != s:
#     print("Game over")

c = random.randint(1, 3)
if c == 1:
    c = 'r'
elif c == 2:
    c = 'p'
elif c == 3:
    c = 's'

print(h, c)

if h == 'r':
    print(rock)
elif h == 'p':
    print(paper)
elif h == 's':
    print(scissors)

if c == 'r':
    print(rock)
elif c == 'p':
    print(paper)
elif c == 's':
    print(scissors)

if (h == 'r' and c == 'r') or (h == 'p' and c == 'p') or (h == 's' and c == 's'):
    print('please repeat')
elif (h == 'r' and c == 's') or (h == 'p' and c == 'r') or (h == 's' and c == 'p'):
    print("Human wins!")
elif (h == 'r' and c == 'p') or (h == 'p' and c == 's') or (h == 's' and c == 'r'):
    print("Computer wins!")


