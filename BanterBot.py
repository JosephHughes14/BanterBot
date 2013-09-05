import twitter

api = twitter.Api(consumer_key = 'xxxx',
                  consumer_secret = 'xxxx',
                  access_token_key = 'xxxx',
                  access_token_secret = 'xxxx')
                  
# get the id of the last tweet retweeted
LATESTFILE = 'banterbot_latest.txt'

file = open(LATESTFILE, "r")
lastid = file.read().strip()
file.close()

#if there is no lastid we need to set it to 0
if lastid == '':
     lastid = 0
     
# perform the search
results = api.GetSearch('banter', since_id=lastid)
if len(results) != 0:
     print 'Found {} results.'.format(len(results))
     
     #grab the tweet with most retweets
     rt_max = 0
     for tweet in results:
          rt_current = tweet.retweet_count
          if rt_current > rt_max:
               rt_max = rt_current
               max_rt_tweet = tweet
               
     print 'HERE IS THE RETWEET COUNT : {}'.format(tweet.retweet_count)
     print 'HERE IS THE TWEET : {}'.format(tweet.text) 
       
else:
     print 'Nothing to reply to. Quitting.'
     
                  
