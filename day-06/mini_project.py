# 🛠️ Mini Project — Student Marks Analyzer

# Marks: [78, 65, 91, 55, 82]

# Highest: 91
# Lowest: 55
# Total: 371
# Average: 74.2
# Passed: 4
# Failed: 1


numbers = []
print("Enter ur Marks one by one... ")
for i in range(0,5):
    if i == 0:
        print("Enter the Marks of English: ", end="" )
        number = int(input())
        numbers.append(number)
    elif i == 1:
        print("Enter the Marks of Maths: ", end="" )
        number = int(input())
        numbers.append(number)
    elif i == 2:
        print("Enter the Marks of Urdu: ", end="" )
        number = int(input())
        numbers.append(number)
    elif i == 3:
        print("Enter the Marks of Physics: ", end="" )
        number = int(input())
        numbers.append(number)
    elif i == 4:
        print("Enter the Marks of Chemistry: ", end="" )
        number = int(input())
        numbers.append(number)


print("Marks:", numbers)

# for highest marks

largest = numbers[0]

if largest < numbers[1]:
    largest = numbers[1]
if largest < numbers[2]:
    largest = numbers[2]
if largest < numbers[3]:
    largest = numbers[3]
if largest < numbers[4]:
    largest = numbers[4]


print("Heighest Marks in subjects obtain is: ", largest)

# for lowest marks

smallest = numbers[0]

if smallest > numbers[1]:
    smallest = numbers[1]
if smallest > numbers[2]:
    smallest = numbers[2]
if smallest > numbers[3]:
    smallest = numbers[3]
if smallest > numbers[4]:
    smallest = numbers[4]



print("Lowest Marks in subjects obtain is: ", smallest)

# sum of all marks

total = 0
total = numbers[0]
for i in range (0,5):
    total = total + numbers[i]

print("Sum of Marks", total)

# average
avg = 0

avg = total/len(numbers)

print("avg of all marks", avg)

# passed or fail..?
passed = 0
failed = 0

for i in range(0,5):
    if numbers[i]> 50:
        passed += 1
    elif numbers[i] < 50:
        failed += 1

print("Passed Subjects", passed)
print("Failed Subjects", failed)
