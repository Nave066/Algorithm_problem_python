import random


def random_guess(random_value):
    count = 1
    guess = int(input("Enter your guess: "))
    while guess != random_value:
        if guess > random_value:
            print("Your guess is higher!!")
        else:
            print("Your guess is lower!!")
        guess = int(input("Enter Again: "))
        count += 1
    print("You guessed Correctly")
    return count


if __name__ == "__main__":
    rand = random.randint(1, 101)
    print("It took {} turns to guess the correct one".format(random_guess(rand)))
