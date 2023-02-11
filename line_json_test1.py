from cgitb import handler
from flask_ngrok import run_with_ngrok
from flask import Flask, request
import json
from linebot.models import TextMessage,MessageEvent,TextSendMessage
from linebot import LineBotApi,WebhookHandler

# 查看line 回復裡的json 格式


app = Flask(__name__)
handler=WebhookHandler('2c70b7d37347804b9d7806ae44040598')
line_bot_api=LineBotApi('TeQd4PjfhKAOszYj30cvcBWwGlEcngP1cZh3y3uFAt8lOuqBwUhX39hNpP5J7PMbxYvqG9QEQg4UtUHvlUHTyZvtP1nC2xuSrDqn1/OT5OmJDoPgRpOkZcbF2dh5q1MtoMu63Sa9Oqvhzj4jLLXaCwdB04t89/1O/w1cDnyilFU=')


@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)               # 印出 json_data
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user id when reply
    user_id = event.source.user_id
    print("user_id =", user_id)
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
    
if __name__ == "__main__":
    run_with_ngrok(app)
    app.run()
    