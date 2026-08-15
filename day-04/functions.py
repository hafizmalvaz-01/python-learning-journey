#find maximum number

def maximum(p1, p2):

    if (p1 > p2):
        large = p1
        return large
    else:
        large = p2
        return large

def ask_number():
    print("Enter the Number:   ", end="")
    value = int(input())
    return value

largest = 0
for i in range (1,6):
    print("You're entering ", i , "number")
    new_number = ask_number()
    largest = maximum(largest, new_number)

print("Largest: ", largest)




#find minimum number

def minimum(p1, p2):

    if (p1 > p2):
        small = p2
        return small
    else:
        small = p1
        return small

def ask_number():
    print("Enter the Number:   ", end="")
    value = int(input())
    return value

# smallest = 0
print("You're entering 1 number")
smallest = ask_number()
for i in range (2,6):
    print("You're entering ", i , "number")
    new_number = ask_number()
    smallest = minimum(smallest, new_number)

print("Smallest: ", smallest)