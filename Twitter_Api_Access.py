import tweepy
import time

consumer_key = 'fg6RY23iaTztDOuUUxSy5REdM'
consumer_secret = 'eB4A94FKBoITvcbtD7a1twvMRR1QcXOLuLqPCG67ccjoCvVBf9'
access_token = '1504421699206459392-4tMtQJEw5P04xfYFK1Pt1RnYxDZaFB'
access_token_secret = 'fxHJUaKnVbD0B3gRaTziM5OWLEfj7QRSjyxULnf5Hqsl1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

with open("movies.txt") as f:
    messages = f.readlines()

# Keep track of the current message index
message_index = 0

# Post a message from the file to Twitter every hour
while True:
    # Get the next message from the file
    message = messages[message_index]

    # Post the message to Twitter
    api.update_status(message)

    # Increment the message index, and reset it to 0 if we've reached the end of the file
    message_index += 1
    if message_index >= len(messages):
        message_index = 0

    # Wait for an hour before posting the next message
    time.sleep(3600)

