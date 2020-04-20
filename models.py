import distance as d
from features import *

class TweetsKMeans:
    # m - number of training examples
    # k - number of clusters
    def __init__(self, tweets, k, method):
        self.tweets = tweets
        self.data = features_from_corpus(tweets, method)
        self.m, self.n = self.data.shape
        self.k = k

    def run_k_means(self, iters, type_dist='cosine'):
        centroids = self.initiate_centroids()
        for i in range(0, iters):
            closest_centroids = self.closest_centroids(centroids, type_dist.lower())
            centroids = self.compute_centroids(closest_centroids, type_dist)

        assigned_clusters = self.closest_centroids(centroids, type_dist.lower()).squeeze().astype(int).tolist()
        # finding text tweets centroids
        centroids_text = []
        for c in centroids:
            for i in range(len(self.tweets)):
                if np.array_equal(self.data[i], c):
                    centroids_text.append(self.tweets[i])

        return centroids_text, assigned_clusters

    # computing closest centroid (medoid) for each tweet
    def closest_centroids(self, centroids, type_dist):
        assigned_centroids = np.zeros((self.m, 1))
        for i in range(0, self.m):
            distances = np.zeros((self.k, 1))
            for j in range(0, self.k):
                distances[j] = d.dist(self.data[i], centroids[j], type=type_dist)
            ix = np.argmin(distances)
            assigned_centroids[i] = ix
        return assigned_centroids

    # computing the mean coordinates of assigned points and updating the position of a centroid using that data
    def compute_centroids(self, closest_centroids, type_dist):
        centroids = np.zeros((self.k, self.n))
        for i in range(0, self.k):
            min_dist_tweet = None
            min_dist = math.inf
            tweets_same_centroid = (closest_centroids == i).squeeze()
            for tweet_i in self.data[tweets_same_centroid]:
                dist = 0
                for tweet_j in self.data[tweets_same_centroid]:
                    dist += d.dist(tweet_i, tweet_j, type_dist)
                if dist < min_dist:
                    min_dist = dist
                    min_dist_tweet = tweet_i
            centroids[i] = min_dist_tweet
        return centroids

    # centroids have random positions at the beginning
    def initiate_centroids(self):
        rand_centr_idx = np.random.permutation(self.m)
        centroids = self.data[rand_centr_idx]
        return centroids


class TweetsKMeans2:
    # m - number of training examples
    # k - number of clusters
    def __init__(self, tweets, k, method):
        self.tweets = tweets
        tweets_words_list = []
        for sent in tweets:
            tweets_words_list.append(tweet_obrabiarka(sent, hashowac=0, stemmer=-1))
        self.tweets_words = tweets_words_list
        self.processed_tweets = []
        for sent in tweets:
            self.processed_tweets.append(tweet_obrabiarka(sent, hashowac=0, stemmer=1))
        self.data = features_from_corpus(self.processed_tweets, method)
        self.m, self.n = self.data.shape
        self.k = k

    def run_k_means(self, iters, type_dist='cosine'):
        centroids = self.initiate_centroids()
        for i in range(0, iters):
            closest_centroids = self.closest_centroids(centroids, type_dist.lower())
            centroids = self.compute_centroids(closest_centroids, type_dist)

        assigned_clusters = self.closest_centroids(centroids, type_dist.lower()).squeeze().astype(int).tolist()
        # finding text tweets centroids
        centroids_text = []
        centroids_processed_text = []
        centroids_features = []
        for c in centroids:
            for i in range(len(self.tweets_words)):
                if np.array_equal(self.data[i], c):
                    centroids_text.append(self.tweets_words[i])
                    centroids_processed_text.append(self.processed_tweets[i])
                    centroids_features.append(self.data[i])
                    break
        return centroids_text, centroids_processed_text, centroids_features, group_tweets2(self.tweets, self.tweets_words, assigned_clusters, self.k, self.data)

    # computing closest centroid (medoid) for each tweet
    def closest_centroids(self, centroids, type_dist):
        assigned_centroids = np.zeros((self.m, 1))
        for i in range(0, self.m):
            distances = np.zeros((self.k, 1))
            for j in range(0, self.k):
                distances[j] = d.dist(self.data[i], centroids[j], type=type_dist)
            ix = np.argmin(distances)
            assigned_centroids[i] = ix
        return assigned_centroids

    # computing the mean coordinates of assigned points and updating the position of a centroid using that data
    def compute_centroids(self, closest_centroids, type_dist):
        centroids = np.zeros((self.k, self.n))
        for i in range(0, self.k):
            min_dist_tweet = None
            min_dist = math.inf
            tweets_same_centroid = (closest_centroids == i).squeeze()
            for tweet_i in self.data[tweets_same_centroid]:
                dist = 0
                for tweet_j in self.data[tweets_same_centroid]:
                    dist += d.dist(tweet_i, tweet_j, type_dist)
                if dist < min_dist:
                    min_dist = dist
                    min_dist_tweet = tweet_i
            centroids[i] = min_dist_tweet
        return centroids

    # centroids have random positions at the beginning
    def initiate_centroids(self):
        rand_centr_idx = np.random.permutation(self.m)
        centroids = self.data[rand_centr_idx]
        return centroids


class TweetsRandomClustering:
    # m - number of training examples
    # k - number of clusters
    def __init__(self, tweets, k, method):
        self.tweets = tweets
        self.data = features_from_corpus(tweets, method)
        self.m, self.n = self.data.shape
        self.k = k

    def initiate_centroids(self):
        rand_centr_idx = np.random.permutation(self.m)
        centroids = self.data[rand_centr_idx]
        return centroids

    def run_random_clustering(self, iters, type_dist='jaccard'):
        centroids = self.initiate_centroids()
        assigned_clusters = self.closest_centroids(centroids, type_dist.lower()).squeeze().astype(int).tolist()
        centroids_text = []
        for c in centroids:
            for i in range(len(self.tweets)):
                if np.array_equal(self.data[i], c):
                    centroids_text.append(self.tweets[i])
        return centroids_text, assigned_clusters

    # computing closest centroid (medoid) for each tweet
    def closest_centroids(self, centroids, type_dist):
        assigned_centroids = np.zeros((self.m, 1))
        for i in range(0, self.m):
            distances = np.zeros((self.k, 1))
            for j in range(0, self.k):
                distances[j] = d.dist(self.data[i], centroids[j], type=type_dist)
            ix = np.argmin(distances)
            assigned_centroids[i] = ix
        return assigned_centroids


def group_tweets(tweets, assigned_clusters, k):
    clusters = []
    for i in range(k):
        clusters.append([])
    for i, clstr_id in enumerate(assigned_clusters):
        clusters[clstr_id].append(tweets[i])
    return clusters


def group_tweets2(raw_tweets, processed_tweets, assigned_clusters, k, features):
    raw_clusters = []
    processed_clusters = []
    features_clusters = []
    for i in range(k):
        processed_clusters.append([])
        raw_clusters.append([])
        features_clusters.append([])
    for i, clstr_id in enumerate(assigned_clusters):
        processed_clusters[clstr_id].append(processed_tweets[i])
        raw_clusters[clstr_id].append(raw_tweets[i])
        features_clusters[clstr_id].append(features[i])
    return raw_clusters, processed_clusters, features_clusters
