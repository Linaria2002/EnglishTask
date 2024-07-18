import nltk
from typing import List
from nltk import pos_tag
from nltk.tokenize import word_tokenize
nltk.download("punkt")
nltk.download('averaged_perceptron_tagger')
import accuracy as ACC

word_list = []
target_list = []

def Input_text():
    # Input
    while True:
        try:
            text = input("Enter your text> ")
            word_list.append(text)
            if text == "":
                break
        except EOFError:
            break
    
    # Main process
    for text in word_list:
        words = word_tokenize(text)
        target_words = pos_tag(words)
        target_list.append(target_words)

    return target_list
    
if __name__ == "__main__":
    list = Input_text()
    #print(list)
    ACC.accuracy(list)