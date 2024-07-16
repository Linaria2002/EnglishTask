# 2~4行目はmain.pyで処理するため、後でコメントアウトする
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import CFG

# 助動詞の時制を評価する
def getMDTense(str):
    text = nltk.word_tokenize(str)
    tagged = nltk.pos_tag(text)

    return "Present Tense"

if __name__ == '__main__':
    print(getMDTense("I should go school"))