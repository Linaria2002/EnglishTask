import accuracy as ACC
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
nltk.download("punkt")
nltk.download('averaged_perceptron_tagger')

word_list = []
target_list = []

def Input_text():
    # Input
    while True:
        try:
            text = input("Enter your text> ")
            if text == "":
                break
            word_list.append(text)
        except EOFError:
            break
    
    # Main process
    for text in word_list:
        words = word_tokenize(text)
        target_words = pos_tag(words)
        target_list.append(target_words)

    # Output
    print(ACC.accuracy(target_list))
    print(target_list)
    

if __name__ == "__main__":
    Input_text()