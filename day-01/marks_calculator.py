print("Project 02  Marks Calcultor ")


print (" Enter the marks of following subject out of 100")
print ("English")
engMarks = int(input())

print ("Maths")
mathMarks = int(input())

print( "Computer")
compMarks = int(input())

print ( "Physics" )
phyMarks = int(input())

totalMarks = 400
total = engMarks+mathMarks+compMarks+phyMarks

print ( total, "This is your Total marks!! Congratulations ")

percent = (total/totalMarks)*100

print ( percent, "% This is your total Percentage of these sujects")

