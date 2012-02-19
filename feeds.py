import feedparser
import helpers


class Feeds(object):
    '''
    class that manages the rss feeds fetching
    '''
    def __init__(self, feed_url):
        self.feed_url = feed_url

    def get_feeds(self):
        '''
        returns all the fetched feeds
        '''
        return feedparser.parse(self.feed_url)

    def get_updated_feeds(self, history, last_timestamp):
        '''
        returns new feeds (age-check is done inside a per-feed custom
        function, that should be inside the helpers file)
        '''
        self.updated_timestamp = last_timestamp
        feeds = feedparser.parse(self.feed_url)
        updated_feeds = list()
        check_age = getattr(helpers, history['FUNCTION'])
        for entry in feeds.entries:
            new_timestamp = check_age(getattr(entry, history['FIELD']), \
                last_timestamp)
            if new_timestamp != last_timestamp:
                updated_feeds.append(entry)
                if new_timestamp > self.updated_timestamp:
                    self.updated_timestamp = new_timestamp
        updated_feeds.reverse()
        return updated_feeds

    def get_last_timestamp(self):
        '''
        returns the updated timestamp
        '''
        return self.updated_timestamp
