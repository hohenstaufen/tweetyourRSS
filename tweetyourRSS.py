import sys
import tweepy
import pickle
from bitly import bitly
from twitter import twitter
from feeds import feeds
from settings import *


def main(argv=None):
    '''
    app entry point
    '''
    # gets a twitter object
    tw = twitter(TWITTER['CONSUMER_KEY'], TWITTER['CONSUMER_SECRET'], \
        TWITTER['ACCESS_TOKEN'], TWITTER['ACCESS_TOKEN_SECRET'])
    # gets a bitly object
    bl = bitly(BITLY['USER'], BITLY['APIKEY'])

    # tries to load the history from the file. If an exception is raised,
    # istantiates an empty dictionary object
    try:
        history = pickle.load(open(HISTORY_FILE, 'rb'))
    except:
        history = dict()

    # cycles through the RSSs defined in settings
    for rsskey, rssvalue in RSS.iteritems():
        # gets a feed object
        fd = feeds(rssvalue['RSS'])
        # tries to load last timestamp. If an exception is raised,
        # initializes it with the init value defined in settings
        try:
            last_timestamp = history[rsskey]
        except:
            last_timestamp = (rssvalue['HISTORY'])['INIT_VALUE']
            history[rsskey] = last_timestamp
        # gets the updated feeds
        entries = fd.get_updated_feeds(rssvalue['HISTORY'], last_timestamp)
        # cycles through the feeds, tweetin them
        for feed in entries:
            link = bl.shorten_url(getattr(feed, rssvalue['LINK']))
            tweet = getattr(feed, rssvalue['TEXT'])
            length = TWITTER['TWEET_LENGTH'] - len(rssvalue['HASHTAG']) \
                     - len(link) - 10
            tweet = rssvalue['HASHTAG'] + ' ' + tw.truncate(tweet, length) \
                    + ' ' + link
            tw.update_status(tweet, DEBUG)
        # updates the last timestamp
        history[rsskey] = fd.get_last_timestamp()
    # saves the history
    pickle.dump(history, open(HISTORY_FILE, 'wb'))
    sys.exit(0)

if __name__ == "__main__":
    main()
