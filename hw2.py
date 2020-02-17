#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:00:00 2020

@author: gabylorenzi
"""

#%% 1
#DONE
def longest_path_length(d): 
    """Returns the length of the longest path in d."""
    currMax = 0
    for k,v in d.items():
        path = []
        while(True):
            if (k,v) not in path:
                path.append((k,v))
            else:
                break
            if v in d.keys():
                k = v
                v = d[k]
                l = len(path)
                if l > currMax:
                    currMax = l
            else:
                l = len(path)
                if l > currMax:
                    currMax = l
                break

    return currMax

#%% 2
def large_value_keys(d, N): #DONE
    """Returns a list containing various keys in d.
    
    d is a dictionary who values are ints. N is an int.
    The list contains keys k whose corresponding value d[k] is bigger than N.
    The keys are arranged in order of largest value to smallest value.
    """
    #sort dictionary before hand 
    #sortedDict = {k:v for k,v in sorted(d.items(), key=lambda item: item[1])}
    sortedDict = {r:d[r] for r in sorted(d, key=d.get, reverse = True)}
    L = [k for (k,v) in sortedDict.items() if sortedDict[k] > N]

    return L


#%% 3
#DONE
def count_words(filename):
    """Creates a dictionary from a .txt file counting word occurrences.
    
    For each word in the text file, there's a key.
    The corresponding value is the number of occurrences of the word.
    
    https://docs.python.org/3.7/library/stdtypes.html#string-methods
    
    Capitals are converted to lower case
    so that 'The' does not show up as a key.
    
    Dashes are replaced with spaces
    so that 'them-at' does not show up as a key.
    Both the short dash (-) and long dash (–) are dealt with.
    
    Non-alphabetic characters are stripped from words
    so that “espionage?” does not show up as a key.
    """

    with open(filename) as f:
        novel = f.read()
    #novel = "Hey its gaby# and i am gaby gaby gaby the $$$$ a toad 1234"
    #so novel is just a long string of the entire novel 
    
    #Capitals are converted to lower case
    novel = novel.lower()

    #dashes are replaced with spaces
    novel.replace("-"," ")
    novel.replace("–"," ")
    novel.replace("—"," ")

    #non alphabetic characters are stripped from words
    badchar = '——”‘!@#$%^&*()_“+=-;<:""''>,./?`~[}{]|1234567890'
    for char in badchar:
        novel = novel.replace(char," ")

    #strip
    # char for char in novel if is not char.isalpha()
    words = novel.split()
    frequency = {}

    for word in words:
        if word not in frequency:
            frequency[word] = 0
        frequency[word] +=1
    
    #print(frequency)

    return frequency

# d = count_words('863-0.txt')
# print(d['the'])
# print(2843)
# print(d['i'])
# print(1704)
# print(len({k for k in d if d[k] == 1}))
# print(2665)
# print(large_value_keys(d, 600))

    