import time

import wikipedia
from scipy._lib.six import xrange

import distance
import tweet_cleaner
import features
import database
import wikipedia_breadth_first_search
import helpers

"""
# Wyrzuca wszystkie artykuły pasujące do wyszukiwania
print(wikipedia.search("Bill"))
print(wikipedia.search("Bill", results=1))

print(wikipedia.suggest("Bil cliton"))
print(wikipedia.search(wikipedia.suggest("Bil cliton"), results=1))


sum = wikipedia.summary("Bill Clinton", sentences=1)

tweet = tweet_cleaner.tweet_obrabiarka(sum, 0, 0)
print(features._term_count_in_sentence(tweet))


print(wikipedia.geosearch(51.1, 17.01))

print(wikipedia.page("Wysoka (Wroclaw county)").categories)

print(wikipedia.summary("Wroclaw Clinton"))
"""

wikipedia_database = database.Database(sdow_database='/Users/Adam/Desktop/sdow.sqlite')

page_titles = ['Clinton', 'Wrocław', 'Sea', 'Swimming pool', 'Computer', 'Electricity']
page_ids = helpers.get_page_root_ids_from_titles(wikipedia_database, page_titles)

print(page_ids)

page1_title = wikipedia_database.fetch_page_title(page_ids[0])
page2_title = wikipedia_database.fetch_page_title(page_ids[1])
print(page1_title)
print(page2_title)

start_time1 = time.time()
shortest_paths1 = wikipedia_breadth_first_search.breadth_first_search(page_ids[0], page_ids[1], wikipedia_database)
elapsed_time1 = time.time() - start_time1

print()
print("Shortest paths from "+page1_title+" to "+page2_title)
print(shortest_paths1)
print("Amount of shortest paths: "+str(len(shortest_paths1)))
print("Shortest path length: "+str(len(shortest_paths1[0])-1))
print("Execution time: "+str(elapsed_time1)+" seconds")

start_time2 = time.time()
shortest_paths2 = wikipedia_breadth_first_search.breadth_first_search(page_ids[1], page_ids[0], wikipedia_database)
elapsed_time2 = time.time() - start_time2

print()
print("Shortest paths from "+page2_title+" to "+page1_title)
print(shortest_paths2)
print("Amount of shortest paths: "+str(len(shortest_paths2)))
print("Shortest path length: "+str(len(shortest_paths2[0])-1))
print("Execution time: "+str(elapsed_time2)+" seconds")

start_time3 = time.time()
term_dist = distance.terms_dist(page_titles[0], page_titles[1], wikipedia_database, 'path_len_multiplication')
elapsed_time3 = time.time() - start_time3

print()
print("Distance between "+page_titles[0]+" and "+page_titles[1]+" is: "+str(term_dist))
print("Execution time: "+str(elapsed_time3)+" seconds")

start_time6 = time.time()
term_dist = distance.terms_dist(page_titles[4], page_titles[5], wikipedia_database, 'path_len_multiplication')
elapsed_time6 = time.time() - start_time6

print()
print("Distance between "+page_titles[4]+" and "+page_titles[5]+" is: "+str(term_dist))
print("Execution time: "+str(elapsed_time6)+" seconds")

start_time4 = time.time()
term_dist = distance.terms_dist(page_titles[2], page_titles[3], wikipedia_database, 'path_len_multiplication')
elapsed_time4 = time.time() - start_time4

print()
print("Distance between "+page_titles[2]+" and "+page_titles[3]+" is: "+str(term_dist))
print("Execution time: "+str(elapsed_time4)+" seconds")

start_time5 = time.time()
term_dist = distance.terms_dist(page_titles[2], page_titles[2], wikipedia_database, 'path_len_multiplication')
elapsed_time5 = time.time() - start_time5

print()
print("Distance between "+page_titles[2]+" and "+page_titles[2]+" is: "+str(term_dist))
print("Execution time: "+str(elapsed_time5)+" seconds")


def search_n_grams(tweet, n):
    grams = [tweet[i:i + n] for i in xrange(len(tweet) - n + 1)]
    grams = [' '.join(w for w in word) for word in grams]
    print(grams)


search_n_grams(['Wroclaw', 'jest', 'Ala', 'ma', 'Kota', 'kot', 'ma', 'alę'], 2)
search_n_grams(['Wroclaw', 'jest', 'Ala', 'ma', 'Kota', 'kot', 'ma', 'alę'], 1)


def search_grams(wikipedia_database, tweet):
    lista = []
    licznik = 0
    while licznik < len(tweet) - 1:
        slowo1 = tweet[licznik]
        slowo2 = tweet[licznik + 1]
        bigram = slowo1 + " " + slowo2
        if helpers.page_exists(bigram):
            lista.append(bigram)
            licznik += 2
        elif helpers.page_exists(slowo1):
            lista.append(slowo1)
            licznik += 1
        else:
            licznik += 1
    lista2 = helpers.get_page_root_ids_from_titles(wikipedia_database, lista)
    print(lista2)
    print(lista)


search_grams(wikipedia_database, ['Wroclaw', 'Bil', 'Gates', 'Kioiooass', 'Paris', 'Brussels', 'Trevor', 'Cherry'])
