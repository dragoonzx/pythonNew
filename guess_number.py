import random
x = random.randint(1,10)
howMuch = 0
print('Guess the number from 1 to 10!')
guess = 0
while guess != x:
	howMuch+=1;
	guess = int(input('Your guess is: '))
	if guess > x:
		print('Your number is too high')
	else:
		print('Your number is too low')
print('Yes, you did it! The number is ' + str(guess) + '. You used ' + str(howMuch) + ' guesses.')
