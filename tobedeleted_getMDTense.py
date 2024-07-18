# 2~4行目はmain.pyで処理するため、後でコメントアウトする
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# 助動詞の時制を評価する
def getMDTense(target_list):
    return "Present Tense"

if __name__ == '__main__':
    print(getMDTense("I should go school"))