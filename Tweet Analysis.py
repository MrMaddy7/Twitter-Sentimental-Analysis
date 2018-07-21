import tweepy
from textblob import TextBlob
#Use pip install tweepy 
#use pip install textblob 
final=[]#created a empty list for futher use
positiveCount=0#further use
negativeCount=0#further use
TWITTER_APP_KEY = '' #supply the appropriate keys
TWITTER_APP_KEY_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET =''

auth=tweepy.OAuthHandler(TWITTER_APP_KEY,TWITTER_APP_KEY_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN,TWITTER_ACCESS_TOKEN_SECRET)

api=tweepy.API(auth)

tweets=api.search(q='Trump',count=100)#100 are maximum #trump keyword can be replaced with anyother word

for tweet in tweets:
    
    print(tweet.text)
    ana=TextBlob(tweet.text)
    print(ana.polarity)
    final.append(ana.polarity)

print(final)
print(len(final))

for e in final:
    if e>0:
        positiveCount=positiveCount+1
    elif e<0:
        negativeCount=negativeCount+1
    else:
        pass

if positiveCount>negativeCount:
    print("Positive polarity of tweets")
else:
    print('Negative polarity of tweets')

