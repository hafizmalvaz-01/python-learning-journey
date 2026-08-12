#user INFO


print("Enter username: ")
user = input()
print ("Enter Password")
password = int(input())


#main code


if user == "admin" and password == 1234:
    print("Enter Your Name:_______")
    name = input()
    print("Enter ur ENGLISH marks")
    engMarks = int(input())
    print("Enter ur Computer marks")
    compMarks = int(input())
    print ("enter ur Maths marks")
    mathMarks = int(input())
    print ("Enter ur Physics marks")
    phyMarks = int(input())

    print(name, "Your Details are as below:   ..............")

    total = phyMarks+mathMarks+compMarks+engMarks
    print("Your Total Marks are ", total)

    percent = total/400*100
    print("Your total percentage is ", percent , "%")

else:
    print("Enter valid username and password")