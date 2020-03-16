import distance
import tweet_cleaner

tweet_tokenizer = tweet_cleaner.TweetTokenizer()
tweet_tokens = []

print("Różnica miedzy uwzględnianiem hashtagow a nie, oba ze stemmerem")
aa = tweet_cleaner.tweet_obrabiarka('I’m a Simple Simple Mans boycotts Man. I see things from China, I boycott. #boycottmulan I don’t need #WuhanCoronavirus #ChineseCoronavirus wtever you call it You created the virus and now people are suffering becoz of u', hashowac=0, stemmer=1)
bb = tweet_cleaner.tweet_obrabiarka('I’m a HArd Time time time Mans boycotts Man. I see thing from Poland, I boycott. #boycottmulan I don’t need #WuhanCoronavirus #ChineseCoronavirus wtever you call it You created the virus and now people are suffering becoz of u', hashowac=1, stemmer=1)
print(aa)
print(bb)

text1 = 'Poland :) goes little small good time times'
text2 = 'Poland go battle small good pretime times'
text3 = 'Poland go battle small good pretime times !!!!'
text4 = 'Sweden was good small crab two times/22 :P'

texts = [text1, text2, text3, text4]
print()
print("ZRODLOWE")
print()
print(texts)
print()
print("BEZ STEMMERA")
print()
z_stemmerem = []
for sent in texts:
    z_stemmerem.append(tweet_cleaner.tweet_obrabiarka(sent, hashowac=0, stemmer=0))

print(z_stemmerem)

print()
print("Z STEMMEREM")
print()
bezstemmera = []
for sent in texts:
    bezstemmera.append(tweet_cleaner.tweet_obrabiarka(sent, hashowac=0, stemmer=1))
print(bezstemmera)


print()
print("DYSTANS MIĘDZY TWEETAMI 1 I 2")
print()
bag_of_words = distance.bag_of_words(z_stemmerem)
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
