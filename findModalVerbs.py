# 2~4行目はmain.pyで処理するため、後でコメントアウトする
# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# 助動詞があればそのwordとindexのタプルのリストを返す。
def findModalVerbs(str):
    morph = nltk.word_tokenize(str)
    tagged = nltk.pos_tag(morph)
    # print(tagged)
    res = []
    for i in range(len(tagged)):
        if tagged[i][1] == "MD":
            res.append((tagged[i][0], i))
    return res

if __name__ == '__main__':
    print(findModalVerbs("I should go school"))