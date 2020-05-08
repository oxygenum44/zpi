import distance
import sklearn.metrics as skm
import numpy as np


def elbow(centers, clusters):
    sum = 0
    sum2 = 0
    for klaster in range(len(clusters)):
        for tweet in clusters[klaster]:
            sum = sum + distance.dist(centers[klaster], tweet, type='euclidean')
            sum2 = sum2 + distance.dist(centers[klaster], tweet, type='cosine')
    return sum, sum2


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


def silhoutte(clusters):
    suma = 0
    for klaster in range(len(clusters)):
        for tweet in clusters[klaster]:
            a = average_distance(tweet, clusters[klaster])
            bmin = 999999999
            for k in clusters:
                b = average_distance(tweet, k)
                if b != a and b < bmin:
                    bmin = b
            add = (bmin - a) / max(a, bmin)
            suma = suma + add
    return suma


def calinski_harabasz(clusters):
    data = []
    labels = []
    for cluster_nr in range(len(clusters)):
        for tweet in clusters[cluster_nr]:
            data.append(np.array(tweet))
            labels.append(cluster_nr)
    data = np.array(data)
    print(data.shape)
    print(len(labels))
    return skm.calinski_harabasz_score(data, labels)
