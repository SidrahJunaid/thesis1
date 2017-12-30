#from feature_repr import load_tweets
import re
from nltk.corpus import stopwords

def process_tweets(tweets):
    """
    Some processing taken from: https://www.ravikiranj.net/posts/2012/code/how-build-twitter-sentiment-analyzer/
    :param tweets:
    :return:
    """

    # stop_words = set(stopwords.words('english'))
    stop_words = set([])
    stop_words.update(set(['AT_USER', 'URL', '<user>','<url>']))
    stop_characters = set(['1','2','3','4','5','6','7','8','9',])
    # processed_tweets = set([])  # set to avoid duplicates
    processed_tweets = []
    for tweet in tweets:
        # tweet = tweet[len(tweet.split(',')[0])+1:]   # just for test_data
        tweet = tweet.lower()  # remove capitals
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
        # Convert www.* or https?://* to URL
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
        # Convert @username to AT_USER
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
        # Remove additional white spaces
        tweet = re.sub('[\s]+', ' ', tweet)
        # Replace #word with word
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
        # trim
        tweet = tweet.strip('\'"')
        words = tweet.split(' ')  # split into words
        # define and remove stopwords (i.e. common words)
        # processed_words = []
        # for word in words:
        #     if word not in stop_words:
        #         # if len(stop_characters & set(word)) > 0:  # don't add words that contain stop characters
        #         #     break
        #         word = re.sub('[!@#$,.:/\&;]', '', word)  # remove al punctuation
        #         processed_words.append(word)
        # words = [w.strip('\'"?,.') for w in words if w not in stop_words]
        # if len(processed_words) > 0:
        processed_tweets.append(' '.join(words))
    return list(processed_tweets)





print(process_tweets("@PootieTangMark @joelissiah @G1flight G money don\u2019t be chiple wei give me some bread that way I can do sht like go buy drinks wei"))
