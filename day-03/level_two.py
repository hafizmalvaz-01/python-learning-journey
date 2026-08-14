# Task 4: Find the Largest Number
largest = 0
for i in range(0, 5):
    print("Enter the Number  ", i)
    value = int(input())
    # largest = value
    if value > largest:
        largest = value


print(largest, "This is the ur largest value")


#Task 5: Number Pattern

for i in range (0, 5):
    # print(i) 
    for j in range (0, i):
        print("*", end="")
    print()

#Task 6: Reverse 12345
revNumber = 12345
remain_Num= revNumber
number = 0 
while number <=remain_Num:
    mod_res=remain_Num%10
    print(mod_res, end="")
    remain_Num=remain_Num//10
    # print(remain_Num)
    number = number+1


