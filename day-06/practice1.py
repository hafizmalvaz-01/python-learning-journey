# students = ["Ali", "Ahmed", "Usman"]


# students[0] = "shery"
# (students.append("Alvaz"))

# print("inserting muzammil at index 3", students.insert(3, "Muzammil"))
# print("Count of Ahmed", students.count("Ahmed"))
# print("Finding index of Alvaz", students.index("Alvaz"))


# findindex = students.index("Alvaz")
# print("Before POP",students)
# returned = students.pop(findindex)
# print(returned)
# # (students.remove("Ali"))

# print(students)



# Practice 1 — Lists

# Create:

# numbers = [10, 25, 7, 40, 15]

# Without using max():

# Find the largest number.
# Find the smallest number.
# Calculate the total.
# Calculate the average.

# Don't Google the solution.

numbers = []


for i in range (0,5):
    print("Enter ", i, " Numbers ", end="")
    number = int(input())
    numbers.append(number)

# for i in range (0, 5):
print(numbers)

def check_number( numbers):
    largest = numbers[0]





    # for i in range(0,5):
    #     if numbers[i]>numbers[i+1]:
    #         large = numbers[i]
    #     else:
    #         large = numbers[i+1]
    # return large

check_number(numbers)




