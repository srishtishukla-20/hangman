import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    f=open("words.txt","r")
    data=f.read().split() 
    empty=[]
    for word_list in data:
        empty.append(word_list)
    return empty

def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """

    empty = load_words()
    secret_word = random.choice(empty)
    secret_word = secret_word.lower()

    return secret_word
print(choose_word())