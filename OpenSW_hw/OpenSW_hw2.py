import telegram
import asyncio
import schedule
import time
from datetime import datetime

async def send_message(chat_id, text):
    token = "6804735527:AAFvVD6okO8SVtHL9sI6eLymUSs9VB7GdDw"
    bot = telegram.Bot(token=token)
    await bot.sendMessage(chat_id=chat_id, text=text)

async def send_scheduled_message():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if 6 <= now.hour < 23:
        print("Sending message at", current_time)
        chat_id = "-1001923723841"
        text = "30분뒤에 자동으로 알람해주는 서비스 !!!!!!!"
        await send_message(chat_id, text)

schedule.every(30).minutes.do(lambda: asyncio.run(send_scheduled_message()))

while True:
    schedule.run_pending()
    time.sleep(1)