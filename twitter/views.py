from django.shortcuts import render

# Create your views here.

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import pandas as pd
import csv
import re #regular expression
#from textblob import TextBlob
import string
import tweepy
from rest_framework.decorators import api_view
from rest_framework.response import Response



consumer_key = 'TBMievhvGwYnAxOQXqvBZTJi7'
consumer_secret = 'EQHnudSWMGtAkpSbbBrrA3lv5AR6tOEwg6SWoAF5f4YZxQlblw'
access_token= '1105534627333226496-z16Q4B52lHMnmpk0iQK4i4NBN5cAz7'
access_secret = '9rdz3g9ZGv1w9EgwepjglP8ptysNtZbjzVcDfDafWNmfb'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
from datetime import date
import datetime

today = date.today()

@api_view(['GET'])
def get_tweets(request,name,days):
    d1 = today.strftime("%Y/%m/%d")

    d2 = today - datetime.timedelta(days=days)

    d2 = d2.strftime("%Y/%m/%d")

    date_since = d2
    search_words="#"+str(name)
    tweets = tweepy.Cursor(api.search,q=search_words,lang="en",since=date_since,count=10).items()

    text=[]
    tweet_df = pd.DataFrame()
    df={}

    for tweet in tweets:
        print(tweet.text)
        df['tweet']=tweet.text
        df['username']=tweet.user.name
        tweet_df=tweet_df.append(df,ignore_index=True)

        print("theusername", tweet.user.name)

    return Response(tweet_df)


