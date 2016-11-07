# Use shebang here

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import csv
import sys
import json

class StdOutListener(StreamListener):

    def __init__(self, api = None):
        self.api = api
        self.filename = sys.argv[1]+'_'+time.strftime('%Y%m%d-%H%M%S')+'.csv'
        csvFile = open(self.filename, 'w')

    def on_status(self, status):
        csvFile = open(self.filename, 'a')

        csvWriter = csv.writer(csvFile)

        if not 'RT @' in status.text:
            try:
                csvWriter.writerow([status.text,
                                    status.created_at,
                                    status.geo,
                                    status.lang,
                                    status.place,
                                    status.coordinates,
                                    status.user.favourites_count,
                                    status.user.statuses_count,
                                    status.user.description,
                                    status.user.location,
                                    status.user.id,
                                    status.user.created_at,
                                    status.user.verified,
                                    status.user.following,
                                    status.user.url,
                                    status.user.listed_count,
                                    status.user.followers_count,
                                    status.user.default_profile_image,
                                    status.user.utc_offset,
                                    status.user.friends_count,
                                    status.user.default_profile,
                                    status.user.name,
                                    status.user.lang,
                                    status.user.screen_name,
                                    status.user.geo_enabled,
                                    status.user.profile_background_color,
                                    status.user.profile_image_url,
                                    status.user.time_zone,
                                    status.id,
                                    status.favorite_count,
                                    status.retweeted,
                                    status.source,
                                    status.favorited,
                                    status.retweet_count])
            except Exception as e:
                print(e)
                pass

        csvFile.close()

        return

    def on_error(self, status_code):
        print('Encountered error with status code:', status_code)
        return True

    def on_delete(self, status_id, user_id):
        """Called when a delete notice arrives for a status"""
        print("Delete notice")
        return True

    def on_limit(self, track):
        # If too many posts match our filter criteria and only a subset is sent to us
        print("!!! Limitation notice received")
        return True

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        time.sleep(10)
        return True

def start_mining():

    # Import API Keys
    with open('credentials.json') as creds:
        credentials = json.load(creds)

    #Variables that contains the user credentials to access Twitter API
    consumer_key = credentials['twitter']['cra_twitter_miner_3']['consumer_key']
    consumer_secret = credentials['twitter']['cra_twitter_miner_3']['consumer_secret']
    access_token = credentials['twitter']['cra_twitter_miner_3']['access_token']
    access_token_secret = credentials['twitter']['cra_twitter_miner_3']['access_secret']

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    while True:
        try:
            stream.filter(track=sys.argv[2:])
        except:
            continue
if __name__ == '__main__':
    start_mining()
