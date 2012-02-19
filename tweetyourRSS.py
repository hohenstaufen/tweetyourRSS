#!/usr/bin/env python
'''
tweetyourRSS is a simple python script that enables you to publish any RSS feed
on twitter
'''

import sys
import tweepy
import pickle
from bitly import bitly
from twitter import twitter
from feeds import feeds
from settings import *

__author__ = "Alberto Buratti, Mattia Larentis"
__license__ = "WTFPL"
__maintainer__ = "Alberto Buratti"
__email__ = "alberto.buratti@bluemead.org"


def main():
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
        with open(HISTORY_FILE, 'rb') as history_file:
            history = pickle.load(history_file)
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
    with open(HISTORY_FILE, 'wb') as history_file:
        pickle.dump(history, history_file)
    sys.exit(0)

if __name__ == "__main__":
    main()
