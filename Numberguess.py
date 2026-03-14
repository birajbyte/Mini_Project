import random
jackpot=random.randint(1,100)
guess=int(input("Try to guess the number as soon as possible  "))
count=1
while guess!=jackpot:
    if guess<jackpot:
        print("\nEnter the larger number")
    else:
        print("\nEnter the smaller number")
    guess=int(input("Try to guess again until you get   "))
    count+=1
print(f"\nfinally you got the number {guess}")
print(f"\nThe attemts to guess the number is {count}")