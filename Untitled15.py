#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
from linebot.exceptions import InvalidSignatureError
from linebot import LineBotApi, WebhookHandler
from flask import Flask, request, abort
import random
import sqlite3
import time

app = Flask(__name__)

line_bot_api = LineBotApi(
    'RJGIFQubLtWxNw5V5WU+QiL2/z938XgNAeZH6v5SjxIS17BZPddo4JjPNvGZBTudoUf8BLuR69cwLrOVl9mchkd5oNtWquBBB7nXzA5l9xY/5ITXfS2tQ74528jT9Cm2cQ5FEMszWmb8wEbJUSv8xgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c5f00faed9adaf6e397404d28cdbe096')
a = 0
b = 0


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/callback", methods=['post'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global a, b

    if event.message.text == '現在吃什麼？':
        t = time.localtime()
        current_time = int(time.strftime("%H", t))
        a = 1
        conn = sqlite3.connect('rest.db')

        if current_time < 11 and current_time >= 5:
            b = random.randrange(1, 30)
            sqlite_select_query = "SELECT * FROM shopB WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=record[2]))

        elif current_time < 14 and current_time >= 11:
            b = random.randrange(1, 84)
            sqlite_select_query = "SELECT * FROM shopI WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=record[2]))

        elif current_time < 17 and current_time >= 14:
            b = random.randrange(1, 55)
            sqlite_select_query = "SELECT * FROM shopA WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=record[2]))

        elif current_time < 22 and current_time >= 17:
            b = random.randrange(1, 87)
            sqlite_select_query = "SELECT * FROM shopD WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=record[2]))

        elif current_time <= 2 or current_time >= 22:
            b = random.randrange(1, 14)
            sqlite_select_query = "SELECT * FROM shopM WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=record[2]))

    elif event.message.text == '地址' and a == 1:
        t = time.localtime()
        current_time = int(time.strftime("%H", t))
        a = 2
        conn = sqlite3.connect('rest.db')

        if current_time < 11 and current_time >= 5:
            sqlite_select_query = "SELECT * FROM shopB WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=record[3]))

        elif current_time < 14 and current_time >= 11:
            sqlite_select_query = "SELECT * FROM shopI WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=record[3]))

        elif current_time < 17 and current_time >= 14:
            sqlite_select_query = "SELECT * FROM shopA WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=record[3]))

        elif current_time < 22 and current_time >= 17:
            sqlite_select_query = "SELECT * FROM shopD WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=record[3]))

        elif current_time <= 2 or current_time >= 22:
            sqlite_select_query = "SELECT * FROM shopM WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=record[3]))

    elif event.message.text == '換一家' and a == 1:
        t = time.localtime()
        current_time = int(time.strftime("%H", t))
        a = 1
        conn = sqlite3.connect('rest.db')

        if current_time < 11 and current_time >= 5:
            b = random.randrange(1, 30)
            sqlite_select_query = "SELECT * FROM shopB WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=record[2]))

        elif current_time < 14 and current_time >= 11:
            b = random.randrange(1, 84)
            sqlite_select_query = "SELECT * FROM shopI WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=record[2]))

        elif current_time < 17 and current_time >= 14:
            b = random.randrange(1, 55)
            sqlite_select_query = "SELECT * FROM shopA WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=record[2]))

        elif current_time < 22 and current_time >= 17:
            b = random.randrange(1, 87)
            sqlite_select_query = "SELECT * FROM shopD WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=record[2]))

        elif current_time <= 2 or current_time >= 22:
            b = random.randrange(1, 14)
            sqlite_select_query = "SELECT * FROM shopM WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=record[2]))

    elif event.message.text == '菜單' and a == 1:
        a = 2
        t = time.localtime()
        current_time = int(time.strftime("%H", t))
        a = 1
        conn = sqlite3.connect('rest.db')

        if current_time < 11 and current_time >= 5:
            sqlite_select_query = "SELECT * FROM shopB WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            img = record[4].split(',')
            msg = []
            for i in img:
                path = f'https://raw.githubusercontent.com/GLORYERS/lineBot/master/img/{i}.jpg'
                msg.append(ImageSendMessage(
                    original_content_url=path, preview_image_url=path))

            line_bot_api.reply_message(event.reply_token, msg)

        elif current_time < 14 and current_time >= 11:
            sqlite_select_query = "SELECT * FROM shopI WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            img = record[4].split(',')
            msg = []
            for i in img:
                path = f'https://raw.githubusercontent.com/GLORYERS/lineBot/master/img/{i}.jpg'
                msg.append(ImageSendMessage(
                    original_content_url=path, preview_image_url=path))

            line_bot_api.reply_message(event.reply_token, msg)
        elif current_time < 17 and current_time >= 14:
            sqlite_select_query = "SELECT * FROM shopA WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            img = record[4].split(',')
            msg = []
            for i in img:
                path = f'https://raw.githubusercontent.com/GLORYERS/lineBot/master/img/{i}.jpg'
                msg.append(ImageSendMessage(
                    original_content_url=path, preview_image_url=path))

            line_bot_api.reply_message(event.reply_token, msg)
        elif current_time < 22 and current_time >= 17:
            sqlite_select_query = "SELECT * FROM shopD WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            img = record[4].split(',')
            msg = []
            for i in img:
                path = f'https://raw.githubusercontent.com/GLORYERS/lineBot/master/img/{i}.jpg'
                msg.append(ImageSendMessage(
                    original_content_url=path, preview_image_url=path))

            line_bot_api.reply_message(event.reply_token, msg)

        elif current_time <= 2 or current_time >= 22:
            sqlite_select_query = "SELECT * FROM shopM WHERE Number={}".format(
                b)
            c = conn.execute(sqlite_select_query)
            record = c.fetchone()
            img = record[4].split(',')
            msg = []
            for i in img:
                path = f'https://raw.githubusercontent.com/GLORYERS/lineBot/master/img/{i}.jpg'
                msg.append(ImageSendMessage(
                    original_content_url=path, preview_image_url=path))

            line_bot_api.reply_message(event.reply_token, msg)

    else:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='請重新輸入'))


if __name__ == '__main__':
    app.run()
