from twython import Twython
import json
import os.path

# Uzywajcie tego do pobierania Tweetow
# Jako parametr przyjmuje nazwe hasla wyszukiwania, albo "all" jezeli ma zwrocic wszystkie Tweety
# Aktualnie dostepne sa hasla: cooking, coronavirus, politics, science, sport, tourism, uk, usa
# Zwraca dictionary w postaci: {'user': [], 'date': [], 'full_text': []}
def get_tweets(q):
    dict_ = {'user': [], 'date': [], 'full_text': []}
    if q =="all":
        dict_0 = []
        with open("data/tweets_search-cooking_recent.json", "r") as file:
            dict_ = merge_Dict(dict_, json.load(file))
        with open("data/tweets_search-coronavirus_recent.json", "r") as file:
            dict_ = merge_Dict(dict_, json.load(file))
        with open("data/tweets_search-politics_recent.json", "r") as file:
            dict_ = merge_Dict(dict_, json.load(file))
        with open("data/tweets_search-science_recent.json", "r") as file:
            dict_ = merge_Dict(dict_, json.load(file))
        with open("data/tweets_search-sport_recent.json", "r") as file:
            dict_ = merge_Dict(dict_, json.load(file))
        with open("data/tweets_search-tourism_recent.json", "r") as file:
            dict_ = merge_Dict(dict_, json.load(file))
        with open("data/tweets_search-uk_recent.json", "r") as file:
            dict_ = merge_Dict(dict_, json.load(file))
        with open("data/tweets_search-usa_recent.json", "r") as file:
            dict_ = merge_Dict(dict_, json.load(file))

        oc_set = set()
        res = []
        for idx, val in enumerate(dict_['full_text']):
            if val not in oc_set:
                oc_set.add(val)
            else:
                res.append(idx)

        for index in sorted(res, reverse=True):
            del dict_['user'][index]
            del dict_['date'][index]
            del dict_['full_text'][index]
        #print(get_duplicates(dict_))
    else:
        if os.path.isfile("data/tweets_search-" + q + "_recent.json"):
            with open("data/tweets_search-" + q + "_recent.json", "r") as file:
                dict_ = json.load(file)
        else:
            raise ValueError("Wrong search parameter value. Use one of these: {cooking, coronavirus, politics, science, sport, tourism, uk, usa, all}")
    return dict_

def get_duplicates(dict_):
    duplicates = []
    for item in dict_['full_text']:
        if dict_['full_text'].count(item) > 1:
            duplicates.append(item)
    return duplicates


def download_tweets(q):
    with open("data/twitter_credentials.json", "r") as file:
        creds = json.load(file)

    python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
    query = {'q': q + '-filter:retweets',
             'count': 100,
             'lang': 'en',
             'tweet_mode': 'extended'
             }

    dict_1 = {'user': [], 'date': [], 'full_text': []}
    for status in python_tweets.search(**query)['statuses']:
        dict_1['user'].append(status['user']['screen_name'])
        dict_1['date'].append(status['created_at'])
        dict_1['full_text'].append(status['full_text'])

    if os.path.isfile("data/tweets_search-" + q + "_recent.json"):
        with open("data/tweets_search-" + q + "_recent.json", "r") as file:
            dict_2 = json.load(file)

        dict_2['user'].extend(dict_1['user'])
        dict_2['date'].extend(dict_1['date'])
        dict_2['full_text'].extend(dict_1['full_text'])

        oc_set = set()
        res = []
        for idx, val in enumerate(dict_2['full_text']):
            if val not in oc_set:
                oc_set.add(val)
            else:
                res.append(idx)

        for index in sorted(res, reverse=True):
            del dict_2['user'][index]
            del dict_2['date'][index]
            del dict_2['full_text'][index]
        print(get_duplicates(dict_2))

        with open("data/tweets_search-" + q + "_recent.json", "w") as file:
            json.dump(dict_2, file)
    else:
        with open("data/tweets_search-" + q + "_recent.json", "w") as file:
            json.dump(dict_1, file)


def save_credentials():
    credentials = {}
    credentials['CONSUMER_KEY'] = "iQzntFMsJIT5FflAentuzr4qc"
    credentials['CONSUMER_SECRET'] = "BfLjeFFfE0inLmNdGgdXeGKLV7EVUfmemKFJT0DmA1sjpzXCoD"
    credentials['ACCESS_TOKEN'] = "1236345573248241664-lmG17xupjGvT33mdNFOOcGvdyNehnU"
    credentials['ACCESS_SECRET'] = "CdFfUw6bP4hXgAqkHTKUwPVFLR5c00YLh73K7eh0yIGvi"

    with open("twitter_credentials.json", "w") as file:
        json.dump(credentials, file)


def merge_Dict(dict1, dict2):
    dict3 = {}
    for key in set().union(dict1, dict2):
        if key in dict1 : dict3.setdefault(key, []).extend(dict1[key])
        if key in dict2 : dict3.setdefault(key, []).extend(dict2[key])
    return dict3


download_tweets('cooking')
print(get_tweets("cooking"))



