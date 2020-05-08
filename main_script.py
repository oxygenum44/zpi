from wordcloud import WordCloud
import matplotlib.pyplot as plt
import models
import naming
import twitterAPI
from tweet_cleaner import tweet_obrabiarka
import itertools
import model_selection

tweets = twitterAPI.get_tweets('uk')['full_text']
tweets2 = twitterAPI.get_tweets('cooking')['full_text']
tweets3 = twitterAPI.get_tweets('science')['full_text']
tweets4 = twitterAPI.get_tweets('australia')['full_text']
tweets5 = twitterAPI.get_tweets('tourism')['full_text']
tweets6 = twitterAPI.get_tweets('sport')['full_text']
print(len(tweets))
tweets = tweets[int(len(tweets) / 1.2):]
print(len(tweets))
tweets2 = tweets2[int(len(tweets2) / 1.025):]
print(len(tweets2))
tweets3 = tweets3[int(len(tweets3) / 1.2):]
print(len(tweets3))
tweets4 = tweets4[int(len(tweets4) / 2):]
print(len(tweets4))
tweets5 = tweets4[int(len(tweets4) / 1.2):]
print(len(tweets5))
tweets6 = tweets4[int(len(tweets4) / 1.2):]
print(len(tweets6))
tweets = tweets + tweets2 + tweets3 + tweets4 + tweets5 + tweets6
print(len(tweets))
processedTweets = []
for itr in tweets:
    processedTweets.append(tweet_obrabiarka(itr, hashowac=1, stemmer=1))

# selected_distance_calculating = model_selection.select_distance_calculating(20, tweets, ['euclidean', 'cosine', 'jaccard'])
# print(selected_distance_calculating)

size = [(0, 0), (1, 1), (1, 2), (2, 2), (2, 2), (2, 3), (2, 3), (3, 3), (3, 3), (3, 3), (4, 3), (4, 3), (4, 3), (4, 4),
        (4, 4), (4, 4), (4, 4)]

elbow_wart = []
for i in range(2, 16):
    col, row = size[i]
    centroids_text, centroids_processed_text, centroids_features, (
    raw_tweets_clusters, processed_tweets_clusters, tweet_features_clusters) = models.TweetsKMeans2(tweets, i,
                                                                                                    'tf_idf').run_k_means(
        30, 'cosine')

    cluster_names_one_word = naming.assign_names(processed_tweets_clusters, method="word_one_most_frequent")
    cluster_names_two_words = naming.assign_names(processed_tweets_clusters, method="word_two_most_frequent")
    cluster_names_three_words = naming.assign_names(processed_tweets_clusters, method="word_three_most_frequent")
    cluster_names_one_word_tf_idf = naming.assign_names(processed_tweets_clusters, method="word_one_tf_idf")
    cluster_names_two_words_tf_idf = naming.assign_names(processed_tweets_clusters, method="word_two_tf_idf")
    cluster_names_three_words_tf_idf = naming.assign_names(processed_tweets_clusters, method="word_three_tf_idf")
    """
    print("CENTROIDY:")
    print(centroids_features[0])
    print('Tweety w klastrach')
    for ii in range(len(tweet_features_clusters)):
        print('KLASTER '+cluster_names_two_words[i]+", "+cluster_names_two_words_tf_idf[i])
        for j in range(len(tweet_features_clusters[ii])):
            print(tweet_features_clusters[i][j])
    """
    import analyze

    print("PRINT")
    print(len(centroids_features))
    print(len(tweet_features_clusters))
    elbow_wart.append(analyze.calinski_harabasz(tweet_features_clusters))
    print(elbow_wart)

    fig = plt.figure()
    ile = len(tweet_features_clusters)
    for iii in range(ile):
        ax = fig.add_subplot(col, row, iii + 1,
                             title=str(len(processed_tweets_clusters[iii])) + ", " + cluster_names_two_words_tf_idf[iii])
        tweet_string = " ".join(list(itertools.chain.from_iterable(processed_tweets_clusters[iii])))
        wordcloud = WordCloud().generate(tweet_string)
        ax.imshow(wordcloud)
        ax.axis('off')
    plt.subplots_adjust(0.01, 0.01, 0.99, 0.99, 0.1, 0.1)
    plt.show()


print(elbow_wart)

"""
cluster_names_one_word = naming.assign_names(text_clusters, method="word_one_most_frequent")
cluster_names_two_words = naming.assign_names(text_clusters, method="word_two_most_frequent")
cluster_names_three_words = naming.assign_names(text_clusters, method="word_three_most_frequent")
cluster_names_one_word_tf_idf = naming.assign_names(text_clusters, method="word_one_tf_idf")
cluster_names_two_words_tf_idf = naming.assign_names(text_clusters, method="word_two_tf_idf")
cluster_names_three_words_tf_idf = naming.assign_names(text_clusters, method="word_three_tf_idf")
print('Tweety w klastrach')
for i in range(len(text_clusters)):
    print('KLASTER '+cluster_names_one_word[i]+", "+cluster_names_two_words[i]+", "+cluster_names_three_words[i]+", "+cluster_names_one_word_tf_idf[i]+", "+cluster_names_two_words_tf_idf[i]+", "+cluster_names_three_words_tf_idf[i])
    for j in range(len(text_clusters[i])):
        print(text_clusters[i][j])
        """
