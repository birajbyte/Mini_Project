#Dice_simulator
import random
total_sum=0
roll_count=0
while True:
    print("\nEnter 1 to roll the dice")
    print("Enter 2 to Exit")
    user_choice=input("Enter the choice 1 or 2  ")
    if user_choice=="1":
        dice_output=random.randint(1,6)
        print(f"Dice rolled and got {dice_output}")
        total_sum+=dice_output
        roll_count+=1
        
    elif user_choice=="2":
        print("Dice rolling stopped")
        break
    else:
        print("invalid choice")
print(f"\nTotal number of times user roll the dice is {roll_count}")
print(f"Sum of the output of the dice is {total_sum}")
    



