from random import randint
import argparse
num_to_guess = randint(0, 100)
parser = argparse.ArgumentParser("Guess a number between 0 and 100.")
parser.add_argument("num")
args = parser.parse_args()


for i in range(5):
    if i == 0:
         user_guess = args.num
    else:
        user_guess = input("your  next guess is:")
    if float(user_guess) == num_to_guess:
        print("Congratulations!")
        break
    elif float(user_guess) < num_to_guess:
        print("It is bigger!")
    elif float(user_guess) > num_to_guess:
        print("It is smaller!")
else:
    print("lost!")

