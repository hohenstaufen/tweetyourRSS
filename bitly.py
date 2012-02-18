import urllib


class bitly:
    '''
    class that manages the bit.ly services
    '''
    def __init__(self, login_user, api_key):
        self.login_user = login_user
        self.api_key = api_key

    def shorten_url(self, long_url):
        '''
        shortens the given url
        '''
        try:
            longUrl = urllib.urlencode(dict(longUrl=long_url))
            login = urllib.urlencode(dict(login=self.login_user))
            apiKey = urllib.urlencode(dict(apiKey=self.api_key))
            encodedurl = "http://api.bit.ly/shorten?version=2.0.1&%s&%s&%s" % \
                       (longUrl, login, apiKey)
            request = urllib.urlopen(encodedurl)
            responde = request.read()
            request.close()
            responde_dict = eval(responde)
            short_url = responde_dict["results"][long_url]["shortUrl"]
            return short_url
        except IOError, e:
            raise "url shortening failed (urllib error)"
