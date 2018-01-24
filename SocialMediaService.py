import twitter
import tweepy
from TwitterModel import TwitterModel
import random
class SocialMediaService:
    """a class which will operate on socail media like Fb and Twitter."""

    def post_random_tweet(self):
        tw_model=TwitterModel()
        auth = tweepy.OAuthHandler(tw_model.API_KEY, tw_model.API_SECTER_KEY)
        auth.set_access_token(tw_model.ACCESS_TOKEN, tw_model.ACCESS_TOKEN_SECTER)
        client = tweepy.API(auth)
        client.update_status(tw_model.get_random_post())
    
    def read_facebook_message(self):
        print('facebook post details')
