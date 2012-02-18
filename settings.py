# enable app debug (currently only output the tweets, without publishing them)
DEBUG = True
# file where the history of the last feed tweeted is kept
HISTORY_FILE = './history.bin'
# bit.ly account configuration
BITLY = {
    'USER': 'YOUR_BIT.LY_USERNAME_HERE',
    'APIKEY': 'YOUR_BIT.LY_API_KEY_HERE',
}
# twitter app configuration
TWITTER = {
    'CONSUMER_KEY': 'YOUR_TWITTER_APP_CONSUMER_KEY_HERE',
    'CONSUMER_SECRET': 'YOUR_TWITTER_APP_CONSUMER_SECRET_HERE',
    'ACCESS_TOKEN': 'YOUR_TWITTER_APP_ACCESS_TOKEN_HERE',
    'ACCESS_TOKEN_SECRET': 'YOUR_TWITTER_APP_ACCESS_TOKEN_SECRET_HERE',
    'TWEET_LENGTH': 140
}
# rss list
RSS = {
    # rss id
    'UNITN_SCIENCE': {
        # rss url
        'RSS': 'http://www.science.unitn.it/cisca/avvisi/feedavvisi.html',
        # hashtag with which the tweet will be tweeted (some redundancy here)
        'HASHTAG': '#unitn',
        # rss link field name
        'LINK': 'link',
        # rss text field name
        'TEXT': 'title',
        # history parameters
        'HISTORY': {
            # field to check to keep the history
            'FIELD': 'link',
            # custom function that is called to check if the feed is newer than
            # the last that has been tweeted during the last run of the app
            'FUNCTION': 'unitn_science',
            # initialization value for the "history" field. Depends on your
            # feed and how you have written your custom function
            'INIT_VALUE': 0,
        }
    }
}

# tries to load the local settings (overriding this file)
try:
    from local_settings import *
except ImportError:
    pass
