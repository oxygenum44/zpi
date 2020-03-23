from tweet_cleaner import tweet_obrabiarka
import math
#Przyjmuje caly tekst jako string
def _term_count_in_sentence_raw(sent):
    sent = tweet_obrabiarka(sent, hashowac=0, stemmer=1)
    freq_table = {}
    for word in sent:
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    return freq_table

#Przyjmuje pokawalkowany string :)
def _term_count_in_sentence(sent):
    freq_table = {}
    for word in sent:
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    return freq_table

#Przyjmuje zbior tweetow jako calych tekstow w postaci string
def _term_count_in_corpus_raw(sentences):
    whole_dict = {}
    for sent in sentences:
        new_dict = _term_count_in_sentence_raw(sent)

        dict3 = {**whole_dict, **new_dict}
        for key, value in dict3.items():
            if key in whole_dict and key in new_dict:
                dict3[key] = value + whole_dict[key]

        whole_dict = dict3
    return whole_dict

#Przyjmuje zbior pokawalkowanych stringow :)
def _term_count_in_corpus(sentences):
    nowy = []
    for sent in sentences:
        nowy.append(tweet_obrabiarka(sent, hashowac=0, stemmer=1))
    dictionary = _term_count_in_corpus_raw(nowy)
    return dictionary

def calculate_tf(sentence):
    tf_list = {}
    count_dict = _term_count_in_sentence(sentence)
    for word in sentence:
        tf_list[word] = (count_dict[word] / len(sentence))
    return tf_list



def ile_zawiera(szukana, korpus):
    licznik = 0
    for document in korpus:
        stan = 0
        for word in document:
            word = word
            if word == szukana:
                stan = 1
        if stan == 1:
            licznik = licznik + 1
    #Żeby uniknąć dzielenia przez 0
    return licznik + 1

def number_of_sentence_in_document(corpus):
    return len(corpus)


def calculate_idf(cutted_sentence, corpus):
    idf_list = {}
    for word in cutted_sentence:
        idf_list[word] = (math.log(number_of_sentence_in_document(corpus) / ile_zawiera(word, corpus)))
    return idf_list

def calculate_tf_idf(sent, corpus):
    tf_idf = {}
    for word in sent:
        tf = calculate_tf(sentence=sent)[word]
        idf = calculate_idf(cutted_sentence=sent, corpus=corpus)[word]
        tf_idf[word] = tf*idf
    return tf_idf

def list_of_all_words_base(corpus):
    lista = set()
    for tweet in corpus:
        for word in tweet:
            lista.add(word)
    return lista

def vector_maker(feature_dict, all_word_list):
    vector = []
    for word in all_word_list:
        wart = feature_dict[word] if word in feature_dict else 0
        vector.append(wart)
    return vector

def tf_idf_feutures_from_corpus(corpus):
    list_of_features = []
    list_of_all_words = list_of_all_words_base(corpus)
    for tweet in corpus:
        tf_idf = calculate_tf_idf(tweet, corpus)
        list_of_features.append(vector_maker(tf_idf, list_of_all_words))
    return list_of_features






