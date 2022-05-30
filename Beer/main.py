from pyrogram import Client, filters
from asyncio import sleep
import os
import random
from telethon.sync import TelegramClient, events
from flask import Flask
app = Flask(__name__)


app = Client("mrteuiuig_account")


api_id = '16890749'
api_hash = 'd5439aaa3ff4ef30696decf6389341ff'
text_sis = '/beer@beerupbot'

TIMEOUT = 3600

@app.on_message(filters.command('/beer@beerupbot', prefixes='.') & filters.me)
async def enable_spam(_, message):
    await message.delete()
    cmd= message.text.split()
    for i in range(int(cmd[1])):
        await message.reply_text(text_sis)
        await sleep(TIMEOUT)
  
if __name__ == '__main__':
    app.run(debug=True)