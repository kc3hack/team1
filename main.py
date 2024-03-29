from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, LocationMessage, ImageMessage
)
import os
import json
from st_main import execute
from io import BytesIO
from PIL import Image
import numpy as np
from predict import execute

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # json6
    tmp = json.loads(body)

    # handle webhook bodya
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    if event.type == "message":

        # botを起動するとき
        if event.message.text == "お腹空いた":
            
            # 選択されたデータを保存する
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text='お好み焼きかたこ焼き、どちらが食べたいですか？'),
                ]
            )
        # 食べたいものを入力してもらった時
        elif event.message.text == "お好み焼き" or event.message.text == "たこ焼き":
           
            f = open('data.txt','a')
            # 選択されたデータを保存する
            f.write(event.message.text+"\n")
            f.close()
            
            file = open('data.txt', "r")
            data = file.readlines()
            print(data)
            file.close()

            # 検索数の入力を求める
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text='現在地から近い順にお店を表示します'),
                    TextSendMessage(text='欲しい店舗の数を教えてください!'),
                ]
            )
            
        # 結果を表示する数を受け取った時
        elif event.message.text.isdecimal():
            # 選択されたデータを保存する
            f = open('data.txt','a')
            f.write(event.message.text+"\n")
            f.close()

            file = open('data.txt', "r")
            data = file.readlines()
            print(data)
            file.close()
            # 位置情報の入力を求める
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text='これから'+data[0]+'のお店を検索するよ！'),
                    TextSendMessage(text='位置情報を送ってね！'),
                    TextSendMessage(text='line://nv/location'),
                ]
            )

        # 例外処理
        else:
            f = open('data.txt','r')
            lines = f.readlines()
            del lines[:]
            f.close()
            line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text='何をいっているのかまるでわからない'),
                ]
            )


# 位置情報を受け取った時
@handler.add(MessageEvent, message=LocationMessage)
def hanndle_get_map(event):
    f = open('data.txt','r')
    lines = f.readlines()
    print(lines)
    data_list = execute(event.message.latitude, event.message.longitude, lines[0], int(lines[1])) 
    f.close()

    file = open("data.txt", "w")
    del lines[:]
    file.close()

    text = []
    for data in data_list:
        if str(data["spend"]).isdecimal():
            text.append(str(data["departure"]) + "駅から" + str(data["arrival"]) + "駅まで電車で移動してそこから徒歩" + str(data["spend"]) + "分にあるお店です。\n" + data["url"])
        else:
            text.append(str(data["spend"]) + "圏内にあるお店です。\n" + data["url"])
   
    return_text = []
    for i in text:
        return_text.append(TextSendMessage(text = i))

    line_bot_api.reply_message(
        event.reply_token,return_text
    )


# 画像を受け取った時
@handler.add(MessageEvent, message=ImageMessage)
def handle_get_picture(event):

    message_id = event.message.id
    message_content = line_bot_api.get_message_content(message_id)

    img_pin = BytesIO(message_content.content)
    image = Image.open(img_pin)
    imgArray = np.asarray(image)
    print(execute(imgArray))

    print(type(imgArray))
       
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
