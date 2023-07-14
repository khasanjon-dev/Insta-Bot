import os

from dotenv import load_dotenv
from instaloader import Instaloader, Profile

load_dotenv('../../.env')
USERNAME = os.getenv('USERNAME_INSTA')


def download_latest_video(username):
    insta = Instaloader()
    profile = Profile.from_username(insta.context, username)
    posts = profile.get_posts()
    latest_post = next(posts, None)
    while latest_post and not latest_post.is_video:
        latest_post = next(posts, None)
    if latest_post:
        insta.download_post(latest_post, target='today')
        print(f'Downloaded !')
    else:
        print('No videos found.')


download_latest_video(USERNAME)
