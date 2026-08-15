def add(p1,p2):
    added = p1+p2
    return added

def subtract(p1, p2):
    subtracted = p1-p2
    return subtracted

def multiply(p1,p2):
    multiplied = p1*p2
    return multiplied

def division(p1,p2):
    if p2 == 0:
        print("division is not possible... <.-.>")
        return 0
    else:
        qoutient = p1/p2
        return qoutient

def even_odd(p1):
    if p1%2 == 0:
        print("Number is Even...")
    else:
        print("Number is ODD...")
    return 0

def neg_pos(p1):
    if p1<0:
        print("Number is Negative....")
    elif p1>0:
        print("Number is Positive....")
    elif p1 == 0:
        print("Number is Zero")
    else:
        print("INvalid number")

    return 0

def square(p1):
    squared = p1*p1
    return squared

def fact(p1):
    value = p1
    for i in range(p1, 0, -1):
        value = value-1
        factorial = value*i
    return factorial

def ask_number():
    print("Enter the Number: ", end="")
    value = int(input())
    return value

#main body

print("System starting .....................................")
print("Enter the value for how many inputs u want(now u are able to add 2 values just): ", end="")
count = int(input())

if count == 1 and count == 2:
# for i in range(0, count):
        value1 = ask_number()
        value2 = ask_number()
# if count ==2:
else:
    print("invalid number")

print("Enter the number which u want to select: \n 1. add\n 2. subtract\n 3. multiply\n 4. division\n 5. odd_even\n 6. negative_positive\n 7. square\n 8. factorial" )
print("Note: if u want 5, 6, 7, 8 enter value in 1.....")
value = int(input())

if value == 1:
    result = add(value1, value2)
elif value == 2:
    result = subtract(value1, value2)
elif value == 3:
    result = multiply(value1, value2)
elif value == 4:
    result = division(value1, value2)
elif value == 5:
    even_odd(value1)
elif value == 6:
    neg_pos(value1)
elif value == 7:
    result = square(value1)
elif value == 8:
    result = fact(value1)
else:
    print("Invalid value enter......")

print("Your result is  ", result)


