print("Enter the word which want to find the number: ", end="")
word = input()
count = len(word)
totalv = 0
totalc = 0


for character in word:
    if character.isalpha():
        if character.lower() in "aeiou":
              totalv = totalv+1
        else:
            totalc = totalc+1


print("Total vowels are: ", totalv)
print("Total consonants are: ", totalc)

#python slicing

print(word[count:0:-1])

# reverse string 

print(word[::-1])