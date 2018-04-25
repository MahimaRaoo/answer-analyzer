import gensim

'''raw_documents = ["","machine learning",
             "Genetic Algorithm (GA) is a search-based optimization technique based on the principles of Genetics and Natural Selection. It is frequently used to find optimal or near-optimal solutions to difficult problems which otherwise would take a lifetime to solve.",
            "Genetic Algorithm (GA) is a search-based optimization technique based on the principles of Genetics and Natural Selection. It is frequently used to find optimal or near-optimal solutions to difficult problems which otherwise would take a lifetime to solve. It is frequently used to solve optimization problems, in research, and in AI.",
            "Genetic Algorithm (GA) is a search-based optimization technique based on the principles of Genetics and Natural Selection. It is frequently used to find optimal or near-optimal solutions to difficult problems which otherwise would take a lifetime to solve. It is frequently used to solve optimization problems, in research, and in machine learning."]
'''
#print("Number of documents:",len(raw_documents))
raw_documents = ["","Genetic Algorithm (GA) is a search-based optimization technique based on the principles of Genetics and Natural Selection. It is frequently used to find optimal or near-optimal solutions to difficult problems which otherwise would take a lifetime to solve. It is frequently used to solve optimization problems, in research, and in machine learning."];
from nltk.tokenize import word_tokenize
gen_docs = [[w.lower() for w in word_tokenize(text)]
            for text in raw_documents]
#print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
#print(dictionary[5])
#print(dictionary.token2id['road'])
#print("Number of words in dictionary:",len(dictionary))
#for i in range(len(dictionary)):
    #print(i, dictionary[i])

corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
#print(corpus)

tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
#print(s)

sims = gensim.similarities.Similarity('D:\AIproject',tf_idf[corpus],num_features=len(dictionary))
#print(sims)
#print(type(sims))
u_inp=str(input("WHAT IS GENETIC ALGORITHM? "))
query_doc = [w.lower() for w in word_tokenize(u_inp)];

#print(query_doc)
query_doc_bow = dictionary.doc2bow(query_doc)
#print(query_doc_bow)
query_doc_tf_idf = tf_idf[query_doc_bow]
#print(query_doc_tf_idf)

s1=list((sims[query_doc_tf_idf]))
print(s1)

if(s1[1]>0.9):
    print(5)
elif(s1[1]>0.8):
    print(4)
elif(s1[1]>0.7):
    print(3)
elif(s1[1]>0.6):
    print(2)
elif(s1[1]>0.5):
    print(1)
else:
    print(0)
#lists1=[x for x in s1.split(" ")]

#print(lists1)


