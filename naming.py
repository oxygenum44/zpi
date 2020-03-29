import operator

import numpy as np

import features
import copy


def assign_names(cleaned_tweets_clusters, method="two_most_frequent"):
    if method == "word_one_most_frequent":
        return assign_name_by_most_frequent(cleaned_tweets_clusters, 1)
    elif method == "word_two_most_frequent":
        return assign_name_by_most_frequent(cleaned_tweets_clusters, 2)
    elif method == "word_three_most_frequent":
        return assign_name_by_most_frequent(cleaned_tweets_clusters, 3)
    elif method == "word_one_tf_idf":
        return assign_name_by_tf_idf(cleaned_tweets_clusters, 1)
    elif method == "word_two_tf_idf":
        return assign_name_by_tf_idf(cleaned_tweets_clusters, 2)
    elif method == "word_three_tf_idf":
        return assign_name_by_tf_idf(cleaned_tweets_clusters, 3)

def assign_name_by_most_frequent(cleaned_tweets_clusters, amount_of_words):
    names = []
    for cluster in cleaned_tweets_clusters:
        words_in_cluster = []
        for tweet in cluster:
            for word in tweet:
                words_in_cluster.append(word)
        if amount_of_words == 1:
            names.append(most_frequent(words_in_cluster))
        elif amount_of_words == 2:
            first_word = most_frequent(words_in_cluster)
            new_list = remove_all(words_in_cluster, first_word)
            second_word = most_frequent(new_list)
            names.append(first_word + "&" + second_word)
        elif amount_of_words == 3:
            first_word = most_frequent(words_in_cluster)
            new_list = remove_all(words_in_cluster, first_word)
            second_word = most_frequent(new_list)
            new_list = remove_all(new_list, second_word)
            third_word = most_frequent(new_list)
            names.append(first_word + "&" + second_word + "&" + third_word)
    return names

def assign_name_by_tf_idf(cleaned_tweets_clusters, amount_of_words):
    all_tweets = []
    names = []
    for cluster in cleaned_tweets_clusters:
        words_in_cluster = []
        for tweet in cluster:
            for word in tweet:
                words_in_cluster.append(word)
            all_tweets.append(tweet)

    all_features_dictionaries = []
    for tweet in all_tweets:
        features_dictionary = features.calculate_tf_idf(tweet, all_tweets)
        all_features_dictionaries.append(features_dictionary)

    clusters_features = []
    for cluster in cleaned_tweets_clusters:
        cluster_features = []
        for i in range(len(all_features_dictionaries)):
            if all_tweets[i] in cluster:
                cluster_features.append(all_features_dictionaries[i])
        clusters_features.append(cluster_features)

    clusters_strengths_dictionaries = []
    for cluster_features in clusters_features:
        cluster_strengths_dictionary = dict()
        for tweet_dict in cluster_features:
            for word in tweet_dict:
                if word in cluster_strengths_dictionary:
                    cluster_strengths_dictionary[word] += tweet_dict[word]
                else:
                    cluster_strengths_dictionary[word] = tweet_dict[word]
        clusters_strengths_dictionaries.append(cluster_strengths_dictionary)

    for cluster_strengths_dictionary in clusters_strengths_dictionaries:
        if amount_of_words == 1:
            names.append(max(cluster_strengths_dictionary.items(), key=operator.itemgetter(1))[0])
        elif amount_of_words == 2:
            first_word = max(cluster_strengths_dictionary.items(), key=operator.itemgetter(1))[0]
            new_dictionary = copy.copy(cluster_strengths_dictionary)
            del new_dictionary[first_word]
            second_word = max(new_dictionary.items(), key=operator.itemgetter(1))[0]
            names.append(first_word + "&" + second_word)
        elif amount_of_words == 3:
            first_word = max(cluster_strengths_dictionary.items(), key=operator.itemgetter(1))[0]
            new_dictionary = copy.copy(cluster_strengths_dictionary)
            del new_dictionary[first_word]
            second_word = max(new_dictionary.items(), key=operator.itemgetter(1))[0]
            del new_dictionary[second_word]
            third_word = max(new_dictionary.items(), key=operator.itemgetter(1))[0]
            names.append(first_word + "&" + second_word + "&" + third_word)

    return names

#https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
def most_frequent(List):
    return max(set(List), key = List.count)


#https://www.includehelp.com/python/remove-all-occurrences-a-given-element-from-the-list.aspx
def remove_all(list, n):
    new_list = copy.copy(list)
    i = 0  # loop counter
    length = len(new_list)
    while i < length:
        if new_list[i] == n:
            new_list.remove(new_list[i])
            length = length - 1
            continue
        i = i + 1
    return new_list