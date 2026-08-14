#Number guessing Game


#hide value

guess = 7



for i in range(3, 0, -1):
    print("Enter any Number:  ")
    value = int(input())
    if value == guess:
        print("You won!!!!!!!!!!!<-.->")
        break
    elif value < guess:
        print("Too Low!")
        print(i-1, "Attempt left")
    elif value > guess:
        print("Too High!")
        print(i-1, "Attempt left")

print("The player has no attempts left.")


