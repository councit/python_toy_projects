import tweepy
from tweepy.auth import OAuthHandler

auth = OAuthHandler("FRwgmkFFzomiC2fqfs2LKQIY0",
                    'oBdIrekCktSAPEMHtPOLiDwPd5zC6uxSqGHF1uCgaUO4Hhwl6R')
auth.set_access_token('175662478-xQ6pVfNgjks3yBDzd21qn82D6biV3CRffPNovTWm',
                      'R2A4htw4iYUDbNAARxxUUkNQN8lK6jAAZhdGeBaxeh38q')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
