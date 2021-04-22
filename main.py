from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser

import random

app = Flask(__name__)

# LINE 聊天機器人的基本資料

line_bot_api = LineBotApi('2KFJDS643elLFG1pgzttD/mx9bBXJHvGeWC5yW2oJhSSmBRtEZUVsKDR+2rSWEq7OEVA4JblV2aGFnjptw4sO5gchKpmATPVOF5arRPbr+/uqYs5h3izIpzOLSyMSSRSSEFUfzIgneeBC66486ckOgdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('c30fc0f17ea1a1aac29d4dfc8039f9ee')


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        handler.handle(body, signature)        
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    message = TextSendMessage(text = event.message.text)
    line_bot_api_reply_message(event.reply_token,message)

if __name__ == "__main__":
    app.run()