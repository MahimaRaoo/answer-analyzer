import nltk
from nltk.corpus import stopwords

from nltk import word_tokenize
sent1=[]
try:
    with open("correctsentences.txt") as f:
        for line in f:
            sent1.append(line)
except UnicodeDecodeError:
    with open("correctsentences.txt",encoding='utf8') as f:
        for line in f:
            sent1.append(line)
sent3=[]
try:
    with open("wrong.txt") as f:
        for line in f:
            sent3.append(line)
except UnicodeDecodeError:
    with open("wrong.txt",encoding='utf8') as f:
        for line in f:
            sent3.append(line)

sent1=str(sent1)
sent3=str(sent3)
stop_words = set(stopwords.words('english'))
sent2= "Genetic Algorithm is a search-based optimization technique pie horse Fares Offer applicable only for users receiving the communication"
list2=nltk.word_tokenize(sent2)

#print(sent1)
#print(sent3)
documents = [(words, "correct")for words in word_tokenize(sent1)if not words in stop_words ]+[(words1, "wrong")for words1 in word_tokenize(sent3)if not words1 in stop_words]


#print(documents)
import random
random.shuffle(documents)
#print(documents)

all_words = []

for w in word_tokenize(sent1+sent3):
    all_words.append(w.lower())

#all_words = nltk.FreqDist(all_words)
print(all_words)
print("**")
word_features = list(all_words)

def find_features(rev):
    #words = set(document)
    #print(words)
    flag=False
    if rev in word_tokenize(sent2):
        flag=True

    return {rev:flag}


featuresets = [(find_features(rev),category) for (rev, category) in documents]

print(featuresets)

training_set = featuresets[100:]
testing_set = featuresets[:100]

classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

#print(find_features("algorithm"))

print(classifier.classify(find_features("algorithm")))


