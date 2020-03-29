import wikipedia
import tweet_cleaner
import features
#Wyrzuca wszystkie artykuły pasujące do wyszukiwania
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
