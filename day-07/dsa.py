# print("enter the number of your table", end="")
# table_number =  int(input())
# for i in range (1, 6):
#     store = table_number * i
#     print( table_number, " x ", i, " = ", store)



# # dsa

# # traversing to find 40
# numbers= [10,20,30,40,50]
# count = -1

# print("enter the digit which want to find from the below list")
# print (numbers)
# value = int(input())

# for number in numbers:
#     count += 1
#     # print(number,"  ", end="")
#     if number == value:
#         found = True
#         print(value, " found at index", count )
#         break

#     elif number != value:
#         found = False

# if found == False:
#     print("value not found")


# # final challenge

numbers = [10, 20, 30, 20, 40, 20, 50]
target = 20
count = 0
index = []
index_count = -1
for number in numbers:
    index_count += 1
    if number == target:
        count += 1
        found = True
        index.append(index_count)
    elif number == target:
        found = False


if found == False:
    print("value not found")


print("Total occurrences: ", count)
print("20 found at indexes: ", index)