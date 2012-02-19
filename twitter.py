import tweepy


class Twitter(object):
    '''
    class that manages the twitter interaction
    '''
    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, \
        ACCESS_SECRET):
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(self.auth)

    def truncate(self, tweet, length=100, suffix='...'):
        '''
        function used to get an "excerpt" from a given text
        '''
        if len(tweet) < length:
            return tweet
        else:
            return ' '.join(tweet[:length + 1].split(' ')[0:-1]) + suffix

    def update_status(self, message, debug=False):
        '''
        tweets the given message
        '''
        if debug:
            print (message + '\n').encode('utf-8')
        else:
            self.api.update_status(message)
