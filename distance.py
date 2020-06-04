import time

import numpy as np

import helpers
import wikipedia_breadth_first_search


def jaccard_distance(bag_of_words_array1, bag_of_words_array2):
    """
    A function calculating jaccard distance between two tweets
    :param bag_of_words_array1: np.array of numbers of occurrences of a word in tweet1 at given place in the list of all words
    :param bag_of_words_array2: np.array of numbers of occurrences of a word in tweet1 at given place in the list of all words
    :return: Number [0;1]
    """
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

    return 1 - (len(sentences_common_set) / len(sentences_sum_set))


def euclidean_distance(bag_of_words_array1, bag_of_words_array2):
    """
    A function calculating euclidean distance between two tweets
    :param bag_of_words_array1: np.array of numbers of occurrences of a word in tweet1 at given place in the list of all words
    :param bag_of_words_array2: np.array of numbers of occurrences of a word in tweet1 at given place in the list of all words
    :return: Number [0;inf)
    """
    root_range = len(bag_of_words_array1)
    squared_subs_sum = 0
    subtraction_list = bag_of_words_array1 - bag_of_words_array2
    for i in range(0, root_range):
        squared_subs_sum += subtraction_list[i] ** 2

    return squared_subs_sum ** (1.0 / float(root_range))


def cosine_distance(bag_of_words_array1, bag_of_words_array2):
    """
    A function calculating cosine distance between two tweets by subtracting their cosine similarity from 1
    :param bag_of_words_array1: np.array of numbers of occurrences of a word in tweet1 at given place in the list of all words
    :param bag_of_words_array2: np.array of numbers of occurrences of a word in tweet1 at given place in the list of all words
    :return: Number [0;1]
    """
    dot = np.dot(bag_of_words_array1, bag_of_words_array2)
    norm1 = np.linalg.norm(bag_of_words_array1)
    norm2 = np.linalg.norm(bag_of_words_array2)
    cos = dot / (norm1 * norm2)
    return 1 - cos


def dist(bag_of_words_array1, bag_of_words_array2, type):
    """
    A function calculating the distance between the tweets based on the name of method of calculating distance
    :param bag_of_words_array1: List of numbers of occurrences of a word in tweet1 at given place in the list of all words
    :param bag_of_words_array2: List of numbers of occurrences of a word in tweet2 at given place in the list of all words
    :return: Number [0;inf), or Number [0;1]
    :return:
    """
    if type == 'jaccard':
        return jaccard_distance(bag_of_words_array1, bag_of_words_array2)
    elif type == 'euclidean':
        return euclidean_distance(bag_of_words_array1, bag_of_words_array2)
    elif type == 'cosine':
        return cosine_distance(bag_of_words_array1, bag_of_words_array2)


def terms_dist(term1, term2, wikipedia_database, type):
    """
    A function calculating the distance between different terms
    :param term1: First term name
    :param term2: Second term name
    :param type: Type of distance calculation
    :return:
    """
    if type == 'path_len_multiplication':
        return path_len_multiplication_term_dist(term1, term2, wikipedia_database)
    else:
        return int('inf')


def path_len_multiplication_term_dist(term1, term2, wikipedia_database):
    page_ids = helpers.get_page_root_ids_from_titles(wikipedia_database, [term1, term2])
    direction1_shortest_paths = wikipedia_breadth_first_search.breadth_first_search(page_ids[0], page_ids[1],
                                                                                    wikipedia_database)
    direction2_shortest_paths = wikipedia_breadth_first_search.breadth_first_search(page_ids[1], page_ids[0],
                                                                                    wikipedia_database)

    dist_befr_normalization = (len(direction1_shortest_paths[0])-1)*(len(direction2_shortest_paths[0])-1)
    print(len(direction1_shortest_paths[0]))
    print(len(direction2_shortest_paths[0]))
    base = 1 - (1 / (dist_befr_normalization + 1))
    print(base)
    return base * base


