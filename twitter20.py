
# coding: utf-8

# In[1]:


get_ipython().system(' pip install tweepy ')


# In[2]:


import tweepy # now we can import


# In[3]:


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream #these things are in tweepy


# In[4]:


consumer_key = 'lol not telling you' #I'm keeping my keys a secret.
consumer_secret = ''
access_token = ''
access_token_secret = ''


# In[ ]:


class StdOutListener(tweepy.StreamListener): #streaming twitter
    # data function
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print("Error status:",status) 
       # handling errors
    
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track=['python', 'javascript', 'ruby'])


# In[ ]:


import json
import pandas as pd
import math.pyplot as plot


# In[ ]:


tweets_file = '../data/twitter_data.txt'
tweets_data = []

tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue #appending tweets to a list from twitter


# In[ ]:


print(len(tweets_data))


# In[ ]:


import re


# In[ ]:


tweets = pd.DataFrame() # defining tweets


# In[ ]:


def word_in_text(word, text):
    word = word.lower(
        text = text.lower()
    match = re.search(word, text)
    if match:
        return True #searching for word
    return False)


# In[ ]:


tweets['python'] = tweets['text'].apply(lambda tweet: word_in_text('python', tweet))
tweets['javascript'] = tweets['text'].apply(lambda tweet: word_in_text('javascript', tweet))
tweets['ruby'] = tweets['text'].apply(lambda tweet: word_in_text('ruby', tweet)) #preparing for next cell


# In[ ]:


print(tweets['python'].value_counts()[True])
print(tweets['javascript'].value_counts()[True])
print(tweets['ruby'].value_counts()[True])


# In[ ]:


prg_langs = ['python', 'javascript', 'ruby']
tweets_by_prg_lang = [tweets['python'].value_counts()[True], tweets['javascript'].value_counts()[True], tweets['ruby'].value_counts()[True]]

x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: python vs. javascript vs. ruby (Raw data)', fontsize=10, fontweight='bold')

ax.set_xticklabels(prg_langs) # graphing bar graph of the popularity of these languages

plt.legend()

plt.show()

