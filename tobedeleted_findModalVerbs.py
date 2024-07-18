# 2~4行目はmain.pyで処理するため、後でコメントアウトする
# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# 助動詞があればそのwordとindexのタプルのリストを返す。
def findModalVerbs(target_list):
    res = []
    for i in range(len(target_list)):
        if target_list[i][1] == "MD":
            res.append((target_list[i][0], i))
    return res

if __name__ == '__main__':
    print(findModalVerbs("I should go school"))