import random

print("H " "A " "N " "G " "M " "A " "N")

#print("The game will be available soon.")

wordlist = ["python", "java", "swift", "javascript"]

comput = random.choice(wordlist)
hint1 = comput[0:3]
hint2 = comput[3:]

h2m=""
for i in hint2:
    i="-"
    h2m=h2m+i

hint =hint1+h2m
print(hint)

guess = input(f"Guess the word {hint}:")



if guess == comput:
    print("You survived!")
else:
    print("You lost!")

