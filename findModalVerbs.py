import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def findModalVerbs(str):
    morph = nltk.word_tokenize(str)
    tagged = nltk.pos_tag(morph)
    print(tagged)
    res = list(filter(lambda x: x[1] == 'MD', tagged))
    return res

if __name__ == '__main__':
    print(findModalVerbs("I should go school"))