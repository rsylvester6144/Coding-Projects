import random
import sys

def elim(num, elim_value, box):
    elim_value = int(elim_value)
    if elim_value > 12:
        while(elim_value > 12):
            elim_value = input(f"Error {elim_value} not in box...Try again: ")
            elim_value = int(elim_value)
        
    if elim_value == num:
        if elim_value in box:
            box.remove(elim_value)
        else:
            print(f"Error: {elim_value} is not in the box.")
    else:
        elim2 = input("Enter number that adds to " + str(num) + ": ")
        elim2 = int(elim2)
        if elim2 not in box:
            print(f"Error: {elim2} is not in the box.")
            return
        if elim_value + elim2 == num:
            box.remove(elim_value)
            box.remove(elim2)
        else:
            print(f"Error: {elim_value} + {elim2} does not equal {num}.")

def gameOver(num, box):
    possible_combinations = [i + j for i in box for j in box if i < j]
    if num not in box and not any(num == i or num in possible_combinations for i in box):
        print("No combinations... GAME OVER")
        sys.exit()

print("#####################################################################################################################\n")
print("Welcome to Shut the Box. The goal of this game is to eliminate every number in the \"box\" by either eliminating the \nnumber rolled on the dice or two numbers that add to the random number. Good luck!\n")
print("#####################################################################################################################\n")

box = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print("Box:\n" + str(box))

while True:
    num = random.randint(1, 12)
    print("\nYou rolled a: " + str(num))
    gameOver(num, box)
    elim_value = input("Enter number to eliminate: ")
    elim(num, elim_value, box)
    print("Updated Box:")
    print(box)
