from twython import Twython
import config

t = Twython(app_key = config.CONSUMER_KEY,
    app_secret = config.CONSUMER_SECRET,
    oauth_token = config.ACCESS_TOKEN,
    oauth_token_secret = config.ACCESS_SECRET)

def post(message):
    t.update_status(status = message)

def post_with_image(message, image_path):
    photo = open(image_path, 'rb')
    response = t.upload_media(media = photo)
    t.update_status(status = message, media_ids = [response['media_is']])

