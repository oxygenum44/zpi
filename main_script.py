from wordcloud import WordCloud
import matplotlib.pyplot as plt
import models
import naming
import twitterAPI
from tweet_cleaner import tweet_obrabiarka
import itertools

tweets = twitterAPI.get_tweets('australia')['full_text']
processedTweets = []
for itr in tweets:
    processedTweets.append(tweet_obrabiarka(itr, hashowac=1, stemmer=1))

centroids_text, centroids_processed_text, centroids_features, (raw_tweets_clusters, processed_tweets_clusters, tweet_features_clusters) = models.TweetsKMeans2(tweets, 8, 'tf_idf').run_k_means(20, 'cosine')

cluster_names_one_word = naming.assign_names(processed_tweets_clusters, method="word_one_most_frequent")
cluster_names_two_words = naming.assign_names(processed_tweets_clusters, method="word_two_most_frequent")
cluster_names_three_words = naming.assign_names(processed_tweets_clusters, method="word_three_most_frequent")
cluster_names_one_word_tf_idf = naming.assign_names(processed_tweets_clusters, method="word_one_tf_idf")
cluster_names_two_words_tf_idf = naming.assign_names(processed_tweets_clusters, method="word_two_tf_idf")
cluster_names_three_words_tf_idf = naming.assign_names(processed_tweets_clusters, method="word_three_tf_idf")

print('Tweety w klastrach')
for i in range(len(tweet_features_clusters)):
    print('KLASTER '+cluster_names_two_words[i]+", "+cluster_names_two_words_tf_idf[i])
    for j in range(len(tweet_features_clusters[i])):
        print(tweet_features_clusters[i][j])

fig = plt.figure()
for i in range(len(processed_tweets_clusters)):
    ax = fig.add_subplot(1, len(processed_tweets_clusters), i+1, title=str(len(processed_tweets_clusters[i]))+", "+cluster_names_two_words_tf_idf[i])
    tweet_string = (" ").join(list(itertools.chain.from_iterable(processed_tweets_clusters[i])))
    wordcloud = WordCloud().generate(tweet_string)
    ax.imshow(wordcloud)
    ax.axis('off')

plt.subplots_adjust(0.01, 0.01, 0.99, 0.99, 0.1, 0.2)
plt.show()
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