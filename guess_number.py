import random

def main():
    n = random.randint(1,100)
    guess_number = []
    while True:
        x = int(input("Guess the number: "))
        if x < 1 or x > 100:
            print("OUT OF BOUNDS!")
        elif 1 <= x <= 100:
            if x == n:
                print(n)
                print("Congratulation! You have guessed the number {} time(s).".format(len(guess_number)))
                print("Guessed numbers: {}".format(guess_number))
                break
            elif abs(x - n) <= 10:
                print("WARM!")
            else:
                print("COLD!")
            guess_number.append(x)
            while True:
                x = int(input("Guess again: "))
                if x < 1 or x > 100:
                    print("OUT OF BOUNDS!")
                elif x == n:
                    print(n)
                    print("Congratulation! You have guessed the number {} time(s).".format(len(guess_number)))
                    print("Guessed numbers: {}".format(guess_number))
                    break
                elif abs(n - x) < abs(n - guess_number[-2]):
                    print("COLDER!")
                elif abs(n - x) > abs(n - guess_number[-2]):
                    print("WARMER!")
                elif abs(x - n) == abs(x - guess_number[-2]):
                    print("AS PREVIOS!")
                

if __name__ == '__main__':
    main()
