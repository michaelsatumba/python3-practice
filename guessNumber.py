import random

print('was up, what is your name?')
name = input()

print('hello ' + name + ' guess the number i have')
secretNumber = random.randint(1, 20)
print(secretNumber)
number = 0


while number < 6:
    number = number + 1
    guess = int(input())
    
    # print(type(guess))
    # print('guess ' + str(guess))
    # print('secretNumber ' + str(secretNumber))
    if guess == secretNumber:
        break
    elif guess < secretNumber:
        print('too low')
        print(str(6 - number) + ' more tries')
    elif guess > secretNumber:
        print('too high')
        print(str(6 - number) + ' more tries')

if number == 1:
    print('you got lucky')
else:
    print('You took ' + str(number) + ' tries')


        

        
