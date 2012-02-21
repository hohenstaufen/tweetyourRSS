from distutils.core import setup

setup(
    name='tweetyourRSS',
    version='0.1.0',
    author='Alberto Buratti',
    author_email='alberthohenstaufen@gmail.com',
    packages=['tweetyourrss', 'tweetyourrss.test'],
    scripts=['bin/tweetyourRSS.py','bin/settings.py', 'bin/helpers.py'],
    url='http://pypi.python.org/pypi/tweetyourRSS/',
    license='LICENSE.txt',
    description='Useful tweetyourrss-related stuff.',
    long_description=open('README.txt').read(),
    install_requires=[
        "feedparser==5.1",
        "tweepy==1.8",
    ],
)
