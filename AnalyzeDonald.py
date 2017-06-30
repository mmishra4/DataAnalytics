#Import the necessary methods from tweepy library
import tweepy
import re
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob

class TwitterClient(object):
    def _init_(self):
        consumer_key = 'zvatCVaqFyTnUIe89bijVrgrh'
        consumer_secret = 'XqL9KcZDjI917jMqfcwOfUwVJNBr7XNLBkNvV65xsWdga34mMg'
        access_token = '879560156060700672-FJz7W3p8diQDiTegiPCKHiZBVQswqCR'
        access_token_secret = 'qgYmuaZjs2GoMzRkvvwuDMzXUmCOJpfjU8wLNXz0hOqdR'
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
            print("Authenticated")
        except:
            print("Error: Authentication failed")
            
    def get_tweets(self, query, max_tweets = 10):
        tweets = []
        searched_tweets = []
        last_id = -1
        while len(searched_tweets) < max_tweets:
            count = max_tweets - len(searched_tweets)
            try:
                new_tweets = api.search(q=query, count=count, max_id=str(last_id - 1))
                if not new_tweets:
                    break
                searched_tweets.extend(new_tweets)
                last_id = new_tweets[-1].id
            except tweepy.TweepError as e:                 
                # depending on TweepError.code, one may want to retry or wait
                # to keep things simple, we will give up on an error
                break
        try:
            for tweet in searched_tweets:
                parsed_tweet = {}
                parsed_tweet['text'] = tweet.text
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                    else:
                        tweets.append(parsed_tweet)
            return tweets
        except tweepy.TweepError as e:
            print("Error : " + str(e))
            
    def clean_tweet(self, tweet):
        pattern = "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"
        parsed_tweet = re.sub(pattern, " ", tweet)
        return " ".join(parsed_tweet.split())
    
    def get_tweet_sentiment(self, tweet):
        pos = 'Positive'
        neg = 'Negative'
        neu = 'Neutral'
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return pos
        elif analysis.sentiment.polarity == 0:
            return neu
        else:
            return neg
        
def main():
    api = TwitterClient()
    tweets = api.get_tweets(query = 'Donald Trump', max_tweets = 10)
    print(tweets)
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'Positive']
    print(ptweets)
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'Negative']
    print(ntweets)
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    neutweets = [tweet for tweet in tweets if tweet['sentiment'] == 'Neutral']    
    print("Neutral tweets percentage: {} %".format(100*len(neutweets)/len(tweets)))
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])


if __name__ == "__main__":
    main()
