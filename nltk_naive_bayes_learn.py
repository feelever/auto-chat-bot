# coding:utf-8
import nltk
from nltk.corpus import names
def gender_features(word):
    return {'suffix1':word[-1],'suffix2':word[-2:]}
def gender_features_update(word):
    features={}
    features["firstletter"]=word[0].lower()
    features["lastletter"]=word[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" % letter]=word.lower().count(letter)
        features["has(%s)" % letter]=(letter in word.lower())
    return features
nam=([(name,'male') for name in names.words('male.txt')]+[(name,'female') for name in names.words('female.txt')])
featuresets=[(gender_features(n),g) for (n,g) in nam]
train_names=nam[1500:]
devtest_names=nam[500:1500]
test_names=nam[:500]
train_set=[(gender_features(n),g) for (n,g) in train_names]
test_set = [(gender_features(n), g) for (n, g) in test_names]
classfier=nltk.NaiveBayesClassifier.train(train_set)
print((classfier.classify(gender_features('neo'))))
print((nltk.classify.accuracy(classfier,test_set)))
print((classfier.show_most_informative_features(5)))
devtest_set = [(gender_features(n), g) for (n, g) in devtest_names]
error=[]
for (name,tag) in devtest_names:
    guess=classfier.classify(gender_features(name))
    if guess != tag:
        error.append((tag,guess,name))
#for (tag,guess,name) in sorted(error):
    #print('correct=%s guess=%s name=%s' % (tag,guess,name))




