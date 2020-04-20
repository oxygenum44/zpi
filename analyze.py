import distance
import numpy as np


def elbow(centers, clusters):
    sum = 0
    for klaster in range(len(clusters)):
        for tweet in clusters[klaster]:
            sum = sum + distance.dist(centers[klaster], tweet, type='euclidean')
    return sum


def average_distance(tweet, klaster):
    suma = 0
    for tweet_itr in klaster:
        suma = suma + distance.dist(tweet, tweet_itr, type='cosine')
    return suma / (len(klaster) - 1) if len(klaster) != 1 else 0.01


def closest_center(centers):
    closest_list = []
    print(centers)
    for center in range(len(centers)):
        min_distance = 9999999999999999
        closest = None
        for center2 in range(len(centers)):
            distance_current = distance.dist(centers[center], centers[center2], type='cosine')
            if distance_current < min_distance and center != center2:
                closest = center2
                min_distance = distance_current
        closest_list.append(closest)
    return closest_list


def silhoutte(centersy, clusters):
    suma = 0
    centersy = np.array(centersy)
    closest_centers = closest_center(centersy)
    for klaster in range(len(clusters)):
        centrum_sasiednie_indeks = closest_centers[klaster]
        for tweet in clusters[klaster]:
            a = average_distance(tweet, clusters[klaster])
            b = average_distance(tweet, clusters[centrum_sasiednie_indeks])
            add = (b - a) / max(a, b)
            suma = suma + add
    return suma
