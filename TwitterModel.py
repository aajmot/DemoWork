import datetime
import random
class TwitterModel:
    now = datetime.datetime.now()
    API_KEY=""
    API_SECTER_KEY=""
    ACCESS_TOKEN=""
    ACCESS_TOKEN_SECTER=""
    TWITTER_POSTS=["Hello #python","have a #great day","not at clock "+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+"","same day, same mistake #dayStory","never give up #positive"]
    
    def __init__(self):
       print('constructor method')

    def get_random_post(self):
        post_len=len(self.TWITTER_POSTS)
        random_no=random.randrange(0,post_len)
        return self.TWITTER_POSTS[random_no]
