import random
guess = ''
while guess not in (1, 0):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    if guess == 'heads':
        guess = 1
    elif guess == 'tails':
        guess = 0
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')