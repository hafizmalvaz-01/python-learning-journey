# 90–100 → A+
# 80–89  → A
# 70–79  → B
# 60–69  → C
# 50–59  → D
# Below 50 → F

print("Enter your Marks 0-100")
marks = int(input())


if 90 <= marks <= 100:
    print(marks, "Obtain A+ Grade")
elif 80 <= marks <= 89:
    print(marks, "Obtain A Grade")
elif 70 <= marks <= 79:
    print(marks, "Obtain B Grade")
elif 60 <= marks <= 69:
    print(marks, "Obtain C Grade")
elif 50 <= marks <= 59:
    print(marks, "Obtain D Grade")
elif 50 >= marks >=0:
    print(marks, "Obtain F Grade")
else:
    print("invalid number")


