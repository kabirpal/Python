import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
print("**********Welcome to the Guessing words game***********")
name = input('Enter your name')
print('Good luck',name.capitalize())

ran_word = random.choice(words)
print(ran_word)

print('~~~~~~~~~~~~~~GAME BEGINS~~~~~~~~~~~~~~~~~')
chance = 12
while chance>0:
    aphla = print('Enter any aplhabet')
    if 