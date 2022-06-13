def find_anagram(word, anagram):
    # [assignment] Add your code here
    strip_word = word.replace(" ", "") # remove spaces
    strip_word = strip_word.lower() # lowercase
    strip_anagram = anagram.replace(" ", "") # remove spaces
    strip_anagram = strip_anagram.lower() # lowercase

    if len(strip_word) != len(strip_anagram):
        #print('False')
        return False
    else:
        for char in strip_anagram:
            if char not in strip_word:
                #print('False')
                return False
            else:
                #print ('True')
                return True
