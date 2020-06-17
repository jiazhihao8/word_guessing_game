from random import choice
word=choice(["code","club"])

guessed=[]
wrong=[]
chance=len(word)+5
while chance>0:
    
    out=""
    for letter in word:
        if letter in guessed:
            out+=letter
        else:
            out+="_"
    if out==word:
        print("You guess is right",word)
        break
    print(chance," chances left")
    print("Guess the word:",out)
    guess=input()
    if guess in guessed or guess in wrong:
        print("Already guessed")
    elif guess in word:
        print("Yes")
        guessed.append(guess)
        chance-=1
    else:
        print("No")
        chance-=1

        wrong.append(guess)
    if chance==0:
        print("You didi not guess", guess)
    print()

    