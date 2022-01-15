from ctypes.wintypes import WORD
import random

def getWord():
    with open ("words.txt", 'r') as f:
        words = f.readlines()
        chosenWord = random.choice(words)
        return(chosenWord)

def hangman():
    word = getWord()
    word_list = []
    tries = len(word)+1
    done = False

    while not done:
        for letter in word:
            #letting player know if the guessed alphabet is present or not
            if letter.lower() in word_list:
                print(letter, end = " ")
            else:
                print("_", end = " ") 

        #telling the player number of tries left
        guess = input(f"Tries: {tries}, Next Guess: ")
        word_list.append(guess.lower())
        if guess.lower() not in word.lower():
            tries -= 1
            if tries == 0:
                break
        
        #figuring out if the guessed alphabets are correct or not
        done = True
        for letter in word:
            if letter.lower() not in word_list:
                done = False

    #telling player if they lost or won the game
    if done:
        print("  ______ ")
        print(" |      |      ")
        print("")
        print(" |      O   ")
        print(" |    / | \ ")    
        print(" |      |   ")
        print(" |     / \   ")
        print(" |    /   \  ")
        print(f"You Won!")
    else:
        print("  ______ ")
        print(" |      |      ")
        print(" |      O   ")
        print(" |    / | \ ")    
        print(" |      |   ")
        print(" |     / \   ")
        print(" |    /   \  ")
        print("You Died! Corect answer was {word}")


#driver code
hangman()
