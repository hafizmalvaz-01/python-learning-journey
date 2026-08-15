#Sum Calculator

print ("Enter the Number for sum: ")
value = int(input())
total = 0

print("")
for i in range(value, 0, -1):
    total = total + i
    # print(i)
    

print(total)



#Factorial Calculator

print ("Enter the Number for factorial: ")
value = int(input())
total = 1

print("")
for i in range(value, 0, -1):
    total = total * i

    

print(total)


#count even and odd numbers total
even = 0
odd = 0
for i in range (0, 10):
    print("Enter the Number ", i, "  ") 
    value = int(input())
    if value%2 ==0:
        even = even + 1
    else:
        odd = odd +1


print("Total number of odd values:  ", odd)
print("Total number of even values:  ", even)

    # print(value)

