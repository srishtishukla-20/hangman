import string
from words import choose_word
from image import IMAGES
def get_hint(secret_word,letters_guessed):

    import random
    letters_not_guessed=[]

    index=0
    while (index<len(secret_word)):
        let=secret_word[index]
        if let not in letters_guessed:
            if let not in letters_not_guessed:
                letters_not_guessed.append(let)
        index+=1
    return random.choice(letters_not_guessed)

def is_word_guessed(secret_word,letters_guessed):
    if secret_word== get_guessed_word(secret_word,letters_guessed):
        return True
    return False

def get_guessed_word(secret_word,letters_guessed):
     index=0
     guessed_word=""
     while (index<len(secret_word)):
         if secret_word[index] in letters_guessed:
             guessed_word+=secret_word[index]
         else:
             guessed_word+="_"
         index+=1

def get_available_letters(letters_guessed):
    import string
    letters_left=string.ascii_lowercase
    for i in letters_guessed:
        letters_left=letters_left.replace(i,"")
    return letters_left
def ifValid(user_input):
    if len(user_input)!=1:
        return False
    if not user_input.isalpha():
        return False
    return True

def hangman(secret_word):

    print("welcome to the Hangman!")
    print("I am thinking of a word that is"+ str(len(secret_word))+"letters long")
    print("")

    user_difficulty_choice=input("How much Difficulty you want to play this game?a= easy,b=medium,c=difficult")
    total_lives=remaining_lives=8
    images_selection_list_indices=[0,1,2,3,4,5,6,7]

    if user_difficulty_choice not in ["a","b","c"]:
        print("Your choice is invalid.\nGame is starting on easy mode")

    else:
        if user_difficulty_choice=="a":
            total_lives=remaining_lives=8
            images_selection_list_indices=[0,1,3,4,5,6,7]

        elif user_difficulty_choice=="b":
            total_lives=remaining_lives=6
            images_selection_list_indices=[0,2,3,5,6,7]
        
        elif user_difficulty_choice=="c":
            total_lives=remaining_lives=4
            images_selection_list_indices=[1,3,5,7]

    letters_guessed=[]

    letters_guessed=[]
    hit=0
    while(remaining_lives>0):
        available_letters=get_available_letters(letters_guessed)
        print("Available Letters:"+available_letters)

        guess=input("Please guess a letter")
        letter=guess.lower()

        if (not ifValid(letter) and letter!="hint"):
            print("Invalid input")
            continue
        if hit==0:
            if guess=="hint":
                p=get_hint(secret_word,letters_guessed)
                print("Your hint for next character",p)
                hit=1
                continue
        if letter in secret_word:
            letters_guessed.append(letter)
            print("good guess:"+get_guessed_word(secret_word,letters_guessed))
            print(" ")

            if is_word_guessed(secret_word,letters_guessed)==True:
                print("* * Congratulations, You Won! * *")
                print(" ")
                break
        
        else:
            print("Oops! That letter is not in my word:"+ get_guessed_word(secret_word,letters_guessed))
            print(IMAGES[8-remaining_lives])
            remaining_lives-=1
            print("Remaining Lives:",remaining_lives)
            print("")
            print(remaining_lives)
            
    else:
        print("Sorry,you ran out of guesses.THe word was"+ str(secret_word))

secret_word=choose_word()
hangman(secret_word)        
