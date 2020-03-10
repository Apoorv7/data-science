import re # regular expression 
import tweepy #access to tweet app
from tweepy import OAuthHandler #authenication 
from textblob import TextBlob #text/tweet parse

def clean_tweet(tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
 

consumer_key = 'TL7RyLnfilYH6xaoAlS0XFDCg'
consumer_secret = 'u5uBn4P62PMIxT4uwUVTl1Ycx4rsfByFs6jl2e4SQ9zDjPIzCO'
access_token = '919434545924935681-2woCDEXuXQdhJewDaCRBqHBYmi5SFDN'
access_token_secret = 'T29jqUm6rZqsRYO7AGc47GlgYTaAaN5OtJD0DATo1uBjh'



auth = OAuthHandler(consumer_key, consumer_secret)
# set access token and secret
auth.set_access_token(access_token, access_token_secret)
# create tweepy API object to fetch tweets
api = tweepy.API(auth)

print(api , ' login success')

leader = ['Narendra Modi','Rahul Gandhi',]

f = open(r'C:\Users\HP\Desktop\output.txt','a')
for l in leader:
    f.write('--------'+l+'----------\n')
    data = api.search(q=l,count=5)
    for d in data:
        print(d.text)
        continue
        try:
            f.write(d.text)
        except:
            f.write('\n')

f.close()

#t1 : good -2, bad  -2 , hello -4

data=open(r'C:\Users\HP\Desktop\output.txt','r')
a=data.readlines()
data.close()
wc=0
w=[]

for l in a:
    w = w + l.split(' ')    
    wc=wc+len(w)
print('------------------------------')
print(w)

counts = dict()
for word in w:
      if word in counts:
          counts[word]+= 1
          
      else:
          counts[word] = 1

print(counts[word])












        
        


        

