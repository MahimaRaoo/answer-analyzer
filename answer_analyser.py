import gensim
raw_documents = ["","ANSWER KEY"];
from nltk.tokenize import word_tokenize
gen_docs = [[w.lower() for w in word_tokenize(text)]
            for text in raw_documents]
dictionary = gensim.corpora.Dictionary(gen_docs)
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
sims = gensim.similarities.Similarity('LOCATION OF DOCUMENT',tf_idf[corpus],num_features=len(dictionary))
u_inp=str(input("QUESTION TO BE ASKED"))
query_doc = [w.lower() for w in word_tokenize(u_inp)]
query_doc_bow = dictionary.doc2bow(query_doc)
query_doc_tf_idf = tf_idf[query_doc_bow]
s1=list((sims[query_doc_tf_idf]))
print(“THE MARKS OBTAINED IS :”)
#here we are considering a 5 marker question

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
