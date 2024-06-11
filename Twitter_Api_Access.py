import tweepy
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Twitter API credentials
consumer_key = '#'
consumer_secret = '#'
access_token = '#'
access_token_secret = '#'

# Authenticate with Twitter
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.verify_credentials()
    logging.info("Authentication successful")
except tweepy.TweepError as e:
    logging.error("Error during authentication", exc_info=True)
    exit(1)

# Load messages from file
try:
    with open("movies.txt") as f:
        messages = f.readlines()
    messages = [message.strip() for message in messages if message.strip()]
    logging.info(f"Loaded {len(messages)} messages")
except Exception as e:
    logging.error("Error reading messages from file", exc_info=True)
    exit(1)

# Configurable sleep time (in seconds)
sleep_time = 3600

# Initialize message index
message_index = 0

# Avoid posting duplicate messages if script restarts
posted_messages = set()

while True:
    try:
        # Check if all messages have been posted
        if message_index >= len(messages):
            logging.info("All messages have been posted. Exiting.")
            break

        # Get the next message from the file
        message = messages[message_index]

        # Post the message to Twitter if it has not been posted before
        if message not in posted_messages:
            api.update_status(message)
            logging.info(f"Posted message: {message}")
            posted_messages.add(message)
        else:
            logging.info(f"Skipping duplicate message: {message}")

        # Increment the message index
        message_index += 1

        # Wait for the specified time before posting the next message
        time.sleep(sleep_time)

    except tweepy.TweepError as e:
        logging.error("Error posting message to Twitter", exc_info=True)
        time.sleep(sleep_time)  # Wait before retrying in case of an error
    except Exception as e:
        logging.error("An unexpected error occurred", exc_info=True)
        break
