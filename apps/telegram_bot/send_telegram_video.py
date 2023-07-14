import os

from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv('../../.env')

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHANNEL_ID')
CHANNEL_USERNAME = os.getenv('CHANNEL_USERNAME')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


async def send_photo_to_telegram_channel(video):
    try:
        with open(video, 'rb') as video:
            text = f' \n\n{CHANNEL_USERNAME}'
            await bot.send_video(chat_id=CHAT_ID, video=video, caption=text)
        print('Video sent successfully to Telegram channel!')
    except Exception as e:
        print(f'Failed to send the video to Telegram channel. Error: {str(e)}')


video_path = '../edit_video/video/watermark_video.mp4'
executor.start(dp, send_photo_to_telegram_channel(video_path))
