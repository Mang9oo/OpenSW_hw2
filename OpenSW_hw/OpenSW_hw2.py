import telegram
import asyncio
import schedule
import time
import datetime
import pytz

token = "6804735527:AAFvVD6okO8SVtHL9sI6eLymUSs9VB7GdDw"
bot = telegram.Bot(token = token)
public_chat_name = "@k20222test"

async def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))

    if now.hour >=23 or now.hour <=6:
        return

    id_channel = await bot.sendMessage(chat_id = public_chat_name, text = "30분뒤에 자동으로 알람해주는 서비스 !!!!!!!")
    print(id_channel)

async def main():
    while True:
        await job()
        await asyncio.sleep(1800)

if __name__ == "__main__":
    asyncio.run(main())
