import models
import distance
import analyze


def select_distance_calculating(clusters_amount, tweets, methods):
    min_silhoutte = float('inf')
    best_method = 'cosine'
    for method in methods:
        centroids_text, centroids_processed_text, centroids_features, (
            raw_tweets_clusters, processed_tweets_clusters, tweet_features_clusters) = models.TweetsKMeans2(tweets,
                                                                                                            clusters_amount,
                                                                                                            'tf_idf').run_k_means(
            20, method)
        silhoutte = analyze.silhoutte(centroids_features, tweet_features_clusters)
        if silhoutte < min_silhoutte:
            min_silhoutte = silhoutte
            best_method = method
    return best_method
