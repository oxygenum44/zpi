import numpy as np

def jaccard_distance(sentence1, sentence2):
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

    return len(sentences_common_set)/len(sentences_sum_set)

def euclidean_distance(bag_of_words1, bag_of_words2):
    root_range = len(bag_of_words1)

    squared_subs_sum = 0
    subtraction_list = bag_of_words1 - bag_of_words2
    for i in range(0, root_range):
        squared_subs_sum += subtraction_list[i]**2

    return squared_subs_sum**(1.0/float(root_range))


def cosine_similarity(sentence1, sentence2):
    return np.dot(sentence1, sentence2) / (np.sqrt(np.dot(sentence1, sentence1)) * np.sqrt(np.dot(sentence2, sentence2)))


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
            if all_words[i] in tweet:
                bag_of_words[i] = 1
        tweets_bags.append(bag_of_words.copy())

    return tweets_bags