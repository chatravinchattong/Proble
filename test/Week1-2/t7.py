import random
print ("***Welcom to the number game***")
number_to_guess = random.randint(1,100)
guess_count = 0
while True:
    user = int(input('Entet your number: '))
    guess_count += 1
    if user <1 or user>100:
        print ("Enter your guess")
    elif user < number_to_guess:
        print ("Too low! Try again!")
    elif user > number_to_guess:
        print ("Too high! Try again!")
    else:
        print (f"Congratulation! You guessed the number in {guess_count}!")
