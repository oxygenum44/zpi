from tweet_cleaner import tweet_obrabiarka
import math
import numpy as np

"""
Module which should be used for feature extracting. 
Outside of module only function:
    features_from_corpus() <--- MAIN
    list_of_all_words_base()
should be used
"""


# Przyjmuje caly tekst jako string
def _term_count_in_sentence_raw(sent):
    """
    This function calculate number of occurences for each word.
    :param sent: one tweet as a String (raw tweet)
    :return: dictionary of pairs like (word, count(word))
    """
    sent = tweet_obrabiarka(sent, hashowac=0, stemmer=1)
    freq_table = {}
    for word in sent:
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    return freq_table


# Przyjmuje pokawalkowany string :)
def _term_count_in_sentence(sent):
    """
    This function calculate number of occurences for each word.
    :param sent: one tweet as a list of words (tweet after tokenization)
    :return: dictionary of pairs like (word, count(word))
    """
    freq_table = {}
    for word in sent:
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    return freq_table


# Przyjmuje zbior tweetow jako calych tekstow w postaci string
def _term_count_in_corpus_raw(sentences):
    """
    This function calculate number of occurences for each word in whole corpus.
    :param sentences: List of tweets (called "corpus") -  (where each tweet is a String)
    :return: dictionary of pairs like (word, count(word)) for whole corpus
    """
    whole_dict = {}
    for sent in sentences:
        new_dict = _term_count_in_sentence_raw(sent)

        dict3 = {**whole_dict, **new_dict}
        for key, value in dict3.items():
            if key in whole_dict and key in new_dict:
                dict3[key] = value + whole_dict[key]

        whole_dict = dict3
    return whole_dict


# Przyjmuje zbior pokawalkowanych stringow :)
def _term_count_in_corpus(sentences):
    """
    This function calculate number of occurences for each word in whole corpus.
    :param sentences: List of tweets (called "corpus") -  (where each tweet is a list of words)
    :return: dictionary of pairs like (word, count(word)) for whole corpus
    """
    nowy = []
    for sent in sentences:
        nowy.append(tweet_obrabiarka(sent, hashowac=0, stemmer=1))
    dictionary = _term_count_in_corpus_raw(nowy)
    return dictionary


def calculate_tf(sentence):
    """
    This function calculate feauture called term frequency.
    :param sentence: Tweet as a list of word
    :return: Dictionary of pairs like (word, word frequency)
    """
    tf_list = {}
    count_dict = _term_count_in_sentence(sentence)
    for word in sentence:
        tf_list[word] = (count_dict[word] / len(sentence))
    return tf_list


def ile_zawiera(szukana, korpus):
    """
    This function calculate how many time word (szukana) occures in whole corpus (set of tweets).
    :param szukana: word, which occurences we want to calculate as a String
    :param korpus: list of tweets (tokenized)
    :return: number of occurences + 1 (in purpose to avoid /0)
    """
    licznik = 0
    for document in korpus:
        stan = 0
        for word in document:
            if word == szukana:
                stan = 1
        if stan == 1:
            licznik = licznik + 1
    # Żeby uniknąć dzielenia przez 0
    return licznik + 1


def number_of_sentence_in_document(corpus):
    """
    This function calculate number of tweets in corpus.
    :param corpus: List of tweets
    :return: Number of tweets in corpus
    """
    return len(corpus)


def calculate_idf(cutted_sentence, corpus):
    """
    This function calculate feature called inversed document (corpus) frequency for one of tweet
    :param cutted_sentence: Sentence (as a List of words) for which we want to find idf
    :param corpus: List of all tweets (each tweet as a list of words)
    :return: Dictionary of pairs (word, idf(word))
    """
    idf_list = {}
    for word in cutted_sentence:
        idf_list[word] = (math.log(number_of_sentence_in_document(corpus) / ile_zawiera(word, corpus)))
    return idf_list


def calculate_tf_idf(tweet, corpus):
    """
    This function calculate feature called tf*idf for one tweet from corpus
    :param tweet: Tweet as a list of words
    :param corpus: List of all tweets (each tweet as a list of words)
    :return: Dictionary of pairs (word, tfidf(word))
    """
    tf_idf = {}
    for word in tweet:
        tf = calculate_tf(sentence=tweet)[word]
        idf = calculate_idf(cutted_sentence=tweet, corpus=corpus)[word]
        tf_idf[word] = tf * idf
    return tf_idf


def list_of_all_words_base(corpus):
    """
    This function let to find all words in whole corpus
    :param corpus: List of all tweets (each tweet as a list of words)
    :return: set of words in corpus
    """
    lista = set()
    for tweet in corpus:
        for word in tweet:
            lista.add(word)
    return lista


def vector_maker(feature_dict, all_word_list):
    """
    This function prepare vector of features.
    :param feature_dict: Dictionary of pairs like (word, some_feature(word))
    :param all_word_list: Set of all words in corpus
    :return: vector of values of features, values have same order as all word list.
    """
    vector = []
    for word in all_word_list:
        wart = feature_dict[word] if word in feature_dict else 0
        vector.append(wart)
    return np.array(vector)


def features_from_corpus(corpus, method):
    """
    This function prepare array of feature vectors. This function should be called outside.
    :param corpus: List of all tweets (each tweet as a list of words)
    :param method: Choice of feature extracting method
    :return: np.array of vectors with feature values for each words in corpus
    """
    list_of_features = []
    list_of_all_words = list_of_all_words_base(corpus)
    for tweet in corpus:
        if method == 'tf_idf':
            dict = calculate_tf_idf(tweet, corpus)
        if method == 'bag_of_word':
            dict = _term_count_in_sentence(tweet)
        list_of_features.append(vector_maker(dict, list_of_all_words))
    return np.array(list_of_features)
