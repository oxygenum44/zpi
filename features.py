from tweet_cleaner import tweet_obrabiarka
import math

text1 = 'Poland :) goes little small good time times'
text2 = 'Poland go battle small good pretime times'
text3 = 'Poland go battle small good pretime times !!!!'
text4 = 'Sweden was good small crab two times/22 :P'

texts = [text1, text2, text3, text4]
nowynowy = []
for itr in texts:
    nowynowy.append(tweet_obrabiarka(itr, hashowac=0, stemmer=1))

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


dict_txt1 = _term_count_in_sentence_raw(text1)
dict_corpus = _term_count_in_corpus_raw(texts)
dict_txt1.update(dict_corpus)
print(dict_txt1)

def calculate_tf(sentence):
    tf_list = []
    count_dict = _term_count_in_sentence(sentence)
    for word in sentence:
        tf_list.append(count_dict[word] / len(sentence))
    return tf_list

print(calculate_tf(nowynowy[0]))


def ile_zawiera(szukana, korpus):
    licznik = 0
    for document in korpus:
        stan = 0
        for word in document:
            if word == szukana:
                stan = 1
        if stan == 1:
            licznik = licznik + 1
    return licznik


def calculate_idf(sentence, korpus):
    idf_list = []
    licznosc_korpusu = len(korpus)
    for word in sentence:
        idf_list.append(math.log(licznosc_korpusu / ile_zawiera(word, korpus)))
    return idf_list


