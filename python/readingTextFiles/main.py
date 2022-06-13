# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string
# each_word_count =[]


def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        contents = f.read()
        # print(contents)
        return contents

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text = text.translate(str.maketrans("", "", string.punctuation))
    each_word_count = {}
    new_text = text.split()
    for word in new_text:
        each_word_count[word] = new_text.count(word)
    # print(each_word_count)
    return each_word_count
read_file_content("./story.txt")
count_words()    
