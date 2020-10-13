# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:15:59 2020

@author: aksha
"""

import json 
from difflib import get_close_matches


def dictionary(word):
    lst = []
    word = word.lower()
    if word in data:
        try:
            lst = (data[word]).splitlines()
            #print(means for means in lst)
            print(f"According to dictionary\n{lst}")
            #return lst
        except:
            #return data['word']
            print(f"According to dictionary\n{data[word]}")
    elif word.title() in data:
        try:
            word = word.title()
            lst = (data[word]).splitlines()
            #print(means for means in lst)
            print(lst)
            #return lst
        except:
            #return data['word']
            print(f"According to the dictionary\n{data[word]}")
    elif word.upper() in data:
        try:
            word = word.upper()
            lst = (data[word]).splitlines()
            #print(means for means in lst)
            print(lst)
            #return lst
        except:
            #return data['word']
            print(f"According to the dictionary\n{data[word]}")
    else:
        print("We couldn't find the word\nDo you mean?")
        print(get_close_matches(word, data, n=2))
        close = get_close_matches(word, data, n=2)
        yn = input("Press y to get the meaning of the suggested words else n:")
        if (yn == 'y'):
            for w in close:
                print(f"According to the dictionary\n{data[w]}")

if __name__ == "__main__":
    with open("D:\\Udacity\\word_meaning.json") as f:
        data = json.load(f)
    #word = input("Enter a word to find its meaning: ")
    #dictionary(word)
    cont = input("Press y to search a word:")
    cont = cont.lower()
    while (cont == 'y'):
        word = input("Enter a word to find its meaning: ")
        dictionary(word)
        cont = input("search again y or n:")
