import random

print("H " "A " "N " "G " "M " "A " "N")


wordlist = ["python", "java", "swift", "javascript"]
count_lost = 0
count_win  = 0


def results():
    print(f"You won: {count_win} times")
    print(f"You lost: {count_lost} times")



def fillup_word(computer, hint, guess):

    for num in range(len(hint)):

        if guess != "":
            if guess in computer:
                ind = computer.find(guess)
                nhint[ind] = guess

            if computer.count(guess) >= 2:
                ind = computer.rfind(guess)
                nhint[ind] = guess

    check = ''.join(nhint)
    return check

def check_if(in_char):
    if len(in_char) != 1:
        x = "Please, input a single letter."
        return x
    if not in_char.islower():
        y = "Please, enter a lowercase letter from the English alphabet."
        return y
    else:
        return True


while True:
    computer = random.choice(wordlist)

    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')

    menu = input()
    if menu=="results":

        results()
        continue
    if menu =="exit":
            exit()
    if menu =="play":
            pass

    hint = ""
    for i in computer:
        dash = "-"
        hint += dash

    print("")
    print(hint)
    nhint = list(hint)
    wordl = []
    guessl = []
    mistake = 0
    while mistake < 8:

        guess = input("Input a letter:")

        if check_if(guess) != True:
            print(check_if(guess))
            print("")

        if check_if(guess) == True:

            guessl.append(guess)
            rep = guessl.count(guess)

            if guess in computer:

                wordl.append(guess)
            if rep > 1:

                print("You've already guessed this letter.")
            elif guess not in computer:
                print("That letter doesn't appear in the word.")
                mistake += 1

        print("")
        print(fillup_word(computer, hint, guess))

        if fillup_word(computer, hint, guess) == computer:
            count_win += 1
            print(f"You guessed the word {computer}!")
            print("You survived!")
            break

        if mistake >= 8:
            count_lost +=1
            print()
            print("You lost!")
            break
