import re
import twitter

api = twitter.Api(consumer_key = 'w3B2jgQKbsbG6thbfmTohA',
                  consumer_secret = 'wXyrJVuFgVPXS8aI17lB60NcDgLLxyCSzCx2afV0w',
                  access_token_key = '1728870349-tmTe6DhTX0RSsMHOSZ54A7gEddDnyNQQ4hjArKA',
                  access_token_secret = 'AkkXjgv359bmuHq8DSlvqxhYz8Lt8AUKKPn6n1lks')

#create an empty hashtag list
hashtags = {}

#Get the home feed
home_feed = api.GetHomeTimeline()

#Easy way to extract hashtags
def extract_hash_tags(post):
	return set(part[1:] for part in post.split() if part.startswith('#'))

#find and append all of the hashtags
for post in home_feed:
	#get the hashtags
	hashtags_in_post = extract_hash_tags(post.text)
	
	#create a key in the dictionary for the user and add the data
	if hashtags_in_post:
		hashtags[post.user.name] = {
				"user" : post.user.name,
				"post" : post.text,
				"hashtags" : hashtags_in_post
				}

#test>>
print "HERE : {}".format(hashtags)
