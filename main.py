import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
nltk.download("punkt")
nltk.download('averaged_perceptron_tagger')

word_list = []
target_list = []

def Input_text():
    while True:
        try:
            text = input("Enter your text")
            word_list.append(text)
            if text == "":
                break
        except EOFError:
            break
    for text in word_list:
        words = word_tokenize(text)
        target_words = pos_tag(words)
        target_list.append(target_words)
    print(target_list)
    

if __name__ == "__main__":
    Input_text()