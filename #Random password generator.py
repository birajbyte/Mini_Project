#Random password generator
import random
import string
while True:
    length=int(input("Enter the length of the password  "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password=""
    for num in range(length):
        password  += random.choice(characters)
    
    print(f"\nPassword is generate",password)
    choice=input("Enter y/Y to generate otherwis press n/N to exit   ")
    if choice.lower() == "n":
        break


        
