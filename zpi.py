import distance
import features
from tweet_cleaner import *
from features import *
import numpy as np
import models
tweet_tokenizer = TweetTokenizer()
tweet_tokens = []

print("Różnica miedzy uwzględnianiem hashtagow a nie, oba ze stemmerem")
aa = tweet_obrabiarka('I’m a Simple Simple Mans boycotts Man. I see things from China, I boycott. #boycottmulan I don’t need #WuhanCoronavirus #ChineseCoronavirus wtever you call it You created the virus and now people are suffering becoz of u', hashowac=0, stemmer=1)
bb = tweet_obrabiarka('I’m a HArd Time time time Mans boycotts Man. I see thing from Poland, I boycott. #boycottmulan I don’t need #WuhanCoronavirus #ChineseCoronavirus wtever you call it You created the virus and now people are suffering becoz of u', hashowac=1, stemmer=1)
print(aa)
print(bb)

text1 = 'Poland :) goes little small small small small good time times ground'
text2 = 'Poland  Poland Poland go battle battle small good pretime times'
text3 = 'Poland go battle small good pretime times !!!!'
text4 = 'Sweden was good small crab two times/22 :P'

texts = [text1, text2, text3, text4]
nowynowy = []
for itr in texts:
    nowynowy.append(tweet_obrabiarka(itr, hashowac=0, stemmer=1))
print()
print("ZRODLOWE")
print()
print(texts)
print()
print("BEZ STEMMERA")
print()
z_stemmerem = []
for sent in texts:
    z_stemmerem.append(tweet_obrabiarka(sent, hashowac=0, stemmer=0))

print(z_stemmerem)

print()
print("Z STEMMEREM")
print()
bezstemmera = []
for sent in texts:
    bezstemmera.append(tweet_obrabiarka(sent, hashowac=0, stemmer=1))
print(bezstemmera)


print()
print("DYSTANS MIĘDZY TWEETAMI 1 I 2")
print()
bag_of_words = distance.bag_of_words(z_stemmerem)
print(bag_of_words)
print("Tweet 1: "+str(z_stemmerem[0])+", BoW: "+str(bag_of_words[0]))
print()
print("Tweet 2: "+str(z_stemmerem[1])+", BoW: "+str(bag_of_words[1]))
print()
print("DYSTANS JACCARDA")
print(distance.jaccard_distance(bag_of_words[0], bag_of_words[1]))
print()
print("DYSTANS EUKLIDESA")
print(distance.euclidean_distance(bag_of_words[0], bag_of_words[1]))
print()
print("DYSTANS COSINE")
print(distance.cosine_similarity(bag_of_words[0], bag_of_words[1]))


print()
print(nowynowy)
print("Demnostracja tf_idf")
print(calculate_tf_idf(sent=nowynowy[0], corpus=nowynowy))

print("Demnostracja BoW")
print(distance.bow(tweet=nowynowy[0]))




#kmeans test
print('----------------KMEANS --------------')
tweet1 = ['poland','poland','poland','poland','good','small','time']
tweet2 = ['poland','poland','poland','bad','big','coronavirus']
tweet3 = ['poland','poland','poland','growth','small','time']
tweet4 = ['poland','poland','poland','bad','big','virus']
tweet5 = ['poland','poland','poland','horrible','small','times']
tweet6 = ['china','china','china','china','poland','poland','coronavirus']
tweet7 = ['china','china','china','china','coronavirus','virus','virus']
tweet8 = ['china','china','china','china','china','china','wuhan']
tweet9 = ['china','china','china','madrid','ronaldo','football','football']
tweet10 = ['china','china','china','china','china','poland','poland']

tweety = [tweet1, tweet2, tweet3, tweet4, tweet5, tweet6, tweet7, tweet8, tweet9, tweet10]
bag = distance.bag_of_words(tweety)

clustering = models.TweetsKMeans(np.asarray(bag), 2)
centroids = clustering.run_k_means(3, 'euclidean')

for i, w1 in enumerate(bag):
    print('Tweet', i)
    print('-----------')
    for j, w2 in enumerate(bag):
        print('Dystans do tweeta', j)
        print(distance.euclidean_distance(w1, w2))
    print('\n')

print("Centroidy")
print('----------')

for i, tweet in enumerate(tweety):
    for centroid in centroids:
        if np.array_equal(bag[i], centroid):
            print(tweet)

print()
print()
print('------------RANDOM CLUSTERING-----------')

clustering = models.TweetsRandomClustering(np.asarray(bag), 2)
centroids = clustering.run_random()

print("Centroidy")
print('----------')

for i, tweet in enumerate(tweety):
    for centroid in centroids:
        if np.array_equal(bag[i], centroid):
            print(tweet)


print("Wszystkie slowa ever w corpusie")

lista_slow = list_of_all_words_base(tweety)
print(lista_slow)

print("Zmiana slownika na feature")
print(calculate_tf_idf(tweet1, tweety))
wektor_feature = vector_maker(calculate_tf_idf(tweet1, tweety), lista_slow)
print(wektor_feature)


print(distance.bow(tweet1))
print(features._term_count_in_sentence(tweet1))

print("Dla bartka")
print(bag)
#print(tf_idf_feutures_from_corpus(tweety))

