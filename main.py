# メインファイル
# botの制御を行う
# coding by rurito

from linebot import LineBotApi
from linebot.models import TextSendMessage

# line botのアクセストークンを持ってくる
# トークン流出を避けるため別のテキストファイルでトークンを管理しています。

def get_token():
    f = open('token.txt')
    lines = f.readline()
    return lines.replace('\n','')

def main():
    
    # トークンを取得
    token = get_token()

    # api読み込み
    line_bot_api = LineBotApi(token)

    user_id = "ruriro0125"
    messages = TextSendMessage(text="進捗出せよ")

    line_bot_api.push_message(user_id, messages)



if __name__ == "__main__":
    main()
