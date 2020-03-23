import numpy as np


def jaccard_distance(bag_of_words_array1, bag_of_words_array2):
    sentence1 = set()
    sentence2 = set()

    for i in range(0, len(bag_of_words_array1)):
        if bag_of_words_array1[i] != 0:
            sentence1.add(str(i))

    for i in range(0, len(bag_of_words_array2)):
        if bag_of_words_array2[i] != 0:
            sentence2.add(str(i))

    sentences_sum_set = set()
    sentences_common_set = set()
    for word in sentence1:
        sentences_sum_set.add(word)
    for word in sentence2:
        sentences_sum_set.add(word)

    for word1 in sentence1:
        for word2 in sentence2:
            if word1 == word2:
                sentences_common_set.add(word1)

    return 1-(len(sentences_common_set) / len(sentences_sum_set))

def euclidean_distance(bag_of_words_array1, bag_of_words_array2):
    root_range = len(bag_of_words_array1)
    squared_subs_sum = 0
    subtraction_list = bag_of_words_array1 - bag_of_words_array2
    for i in range(0, root_range):
        squared_subs_sum += subtraction_list[i]**2

    return squared_subs_sum**(1.0/float(root_range))


def cosine_similarity(bag_of_words_array1, bag_of_words_array2):
    bow_np_arr1 = np.array(bag_of_words_array1)
    bow_np_arr2 = np.array(bag_of_words_array2)
    dot = np.dot(bow_np_arr1, bow_np_arr2)
    norma = np.linalg.norm(bow_np_arr1)
    normb = np.linalg.norm(bow_np_arr2)
    cos = dot / (norma * normb)
    return 1-cos

def bow(tweet):
    all_words = list()
    for word in tweet:
        all_words.append(word)

    bow = {}
    for word in all_words:
        bow.update({word: tweet.count(word)})

    return bow

def bag_of_words(tweets_list):
    all_words_set = set()
    all_words = list()
    for tweet in tweets_list:
        for word in tweet:
            all_words_set.add(word)

    for word in all_words_set:
        all_words.append(word)

    tweets_bags = list()
    for tweet in tweets_list:
        bag_of_words = np.zeros(shape=len(all_words))
        for i in range(len(all_words)):
            bag_of_words[i] += tweet.count(all_words[i])
        tweets_bags.append(bag_of_words.copy())

    return tweets_bags

def dist(bag_of_words1, bag_of_words2, type):
    if type == 'jaccard':
        return jaccard_distance(bag_of_words1, bag_of_words2)
    elif type == 'euclidean':
        return euclidean_distance(bag_of_words1, bag_of_words2)
    elif type == 'cosine':
        return cosine_similarity(bag_of_words1, bag_of_words2)