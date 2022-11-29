from random import randint

def anagram():
    c = []
    
    anagram_word = ""
    
    msg = input("enter your message ").lower().replace(" ", "")
    
    c[:0] = msg # c is a list of all the letters in the message
    
    print(c)
    print(len(c))
    
    rand_char = randint(0, len(msg) - 1) # DEALING WITH INDEX NOT THE REAL LENGTH
    
    for i in range(0, len(c)-1): # as many times as there are characters in input minus 1
        anagram_word += c[rand_char] # randchar is an int. c[rand_char] is a random index of the list c. the letter at the random index appends to the anagram word 
        c.remove(c[rand_char]) # removes the character at the random index in c ("c.remove[randchar]" wouldn't work. c[rand_char] accesses the value at the random index)
        rand_char = randint(0, len(c) - 1) # rassigns the random integer to a number from 0 to the length of the list of characters in the user input - minus one (because it's been removed)
        
    rand_char = 0 # for the list, when there's only one character left in it
    anagram_word += c[rand_char] # appends the character at index 0 from list c to the anagram word
    c.remove(c[rand_char]) # deletes the last character in the list
    
    print(f"{anagram_word = }")
    print(f"{len(anagram_word) = }")

    return anagram_word

anagram()

