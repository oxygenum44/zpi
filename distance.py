import numpy as np

def jaccard_distance(bag_of_words1, bag_of_words2):
    summed_bag_of_words = list(bag_of_words1+bag_of_words2)
    return summed_bag_of_words.count(2)/(len(summed_bag_of_words)-summed_bag_of_words.count(0))

def euclidean_distance(bag_of_words1, bag_of_words2):
    root_range = len(bag_of_words1)
    squared_subs_sum = 0
    subtraction_list = bag_of_words1 - bag_of_words2
    for i in range(0, root_range):
        squared_subs_sum += subtraction_list[i]**2

    return squared_subs_sum**(1.0/float(root_range))


def cosine_similarity(bag_of_words1, bag_of_words2):
    denominator = (np.sqrt(np.dot(bag_of_words1, bag_of_words2)) * np.sqrt(np.dot(bag_of_words2, bag_of_words2)))
    return np.dot(bag_of_words1, bag_of_words2) / denominator


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