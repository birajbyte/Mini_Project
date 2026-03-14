"""Write a python program that will keep adding the stream of numbers
actual format used for billing in market while purchasing"""
sum=0
while True:
    user_input=input("Enter the item price or enter q to exit ")
    if user_input.lower()!="q":
        sum+=int(user_input)
        print(f"Total upto here is  {sum}")
    else:
        print("You have successfully purchased items and press q")
        print(f"The total of items purchase is {sum}")
        break
    


