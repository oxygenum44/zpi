import wikipedia
import wikipediaapi

# import tweet_cleaner
# import features
"""
#Wyrzuca wszystkie artykuły pasujące do wyszukiwania
print(wikipedia.search("Bill"))
print(wikipedia.search("Bill", results=1))

print(wikipedia.suggest("Bil cliton"))
print(wikipedia.search(wikipedia.suggest("Bil cliton"), results=1))


sum = wikipedia.summary("Bill Clinton", sentences=1)

tweet = tweet_cleaner.tweet_obrabiarka(sum, 0, 0)
print(features._term_count_in_sentence(tweet))


print(wikipedia.geosearch(51.0803, 17.01))

print(wikipedia.page("Wysoka (Wroclaw county)").categories)

print(wikipedia.summary("Wroclaw Clinton"))
"""
from scipy._lib.six import xrange


def search_n_grams(tweet, n):
    grams = [tweet[i:i + n] for i in xrange(len(tweet) - n + 1)]
    grams = [' '.join(w for w in word) for word in grams]
    print(grams)


search_n_grams(['Wroclaw', 'jest', 'Ala', 'ma', 'Kota', 'kot', 'ma', 'alę'], 2)
search_n_grams(['Wroclaw', 'jest', 'Ala', 'ma', 'Kota', 'kot', 'ma', 'alę'], 1)

wiki_wiki = wikipediaapi.Wikipedia('en')


def search_grams(tweet):
    lista = []
    lista2 = []
    slowo = []
    licznik = 0
    while licznik < len(tweet) - 1:
        slowo1 = tweet[licznik]
        slowo2 = tweet[licznik + 1]
        bigram = slowo1 + " " + slowo2
        if wiki_wiki.page(bigram).exists():
            lista.append(bigram)
            lista2.append(wikipedia.page(bigram).pageid)
            licznik += 2
        elif wiki_wiki.page(slowo1).exists():
            lista.append(slowo1)
            lista2.append(wikipedia.page(slowo1).pageid)
            licznik += 1
        else:
            licznik += 1
    print(lista2)
    print(lista)


search_grams(['Wroclaw', 'Bil', 'Gates', 'Kioiooass', 'Paris', 'Brussels', 'Trevor', 'Cherry'])
