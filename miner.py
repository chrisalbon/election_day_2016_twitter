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
        self.filename = sys.argv[2]+'_'+time.strftime('%Y%m%d-%H%M%S')+'.csv'
        csvFile = open(self.filename, 'w')
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(['text',
                            'created_at',
                            'geo',
                            'lang',
                            'place',
                            'coordinates',
                            'user.favourites_count',
                            'user.statuses_count',
                            'user.description',
                            'user.location',
                            'user.id',
                            'user.created_at',
                            'user.verified',
                            'user.following',
                            'user.url',
                            'user.listed_count',
                            'user.followers_count',
                            'user.default_profile_image',
                            'user.utc_offset',
                            'user.friends_count',
                            'user.default_profile',
                            'user.name',
                            'user.lang',
                            'user.screen_name',
                            'user.geo_enabled',
                            'user.profile_background_color',
                            'user.profile_image_url',
                            'user.time_zone',
                            'id',
                            'favorite_count',
                            'retweeted',
                            'source',
                            'favorited',
                            'retweet_count'])

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
        if status_code == 401:
            return False

    def on_delete(self, status_id, user_id):
        print("Delete notice")
        return

    def on_limit(self, track):
        print(time.strftime('%H:%M:%S'), "Rate limited, continuing")
        return True

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        time.sleep(10)
        return

def start_mining():

    with open('credentials.json') as creds:
        credentials = json.load(creds)

    consumer_key = credentials['twitter'][sys.argv[1]]['consumer_key']
    consumer_secret = credentials['twitter'][sys.argv[1]]['consumer_secret']
    access_token = credentials['twitter'][sys.argv[1]]['access_token']
    access_token_secret = credentials['twitter'][sys.argv[1]]['access_secret']

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    while True:
        try:
            stream.filter(track=sys.argv[3:])
        except:
            continue
if __name__ == '__main__':
    start_mining()
