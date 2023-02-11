from flask import Flask,request
from flask_ngrok import run_with_ngrok
from linebot import LineBotApi,WebhookHandler
from linebot.models import TextSendMessage

app=Flask(__name__)

@app.route("/")

def home():
    line_bot_api=LineBotApi('TeQd4PjfhKAOszYj30cvcBWwGlEcngP1cZh3y3uFAt8lOuqBwUhX39hNpP5J7PMbxYvqG9QEQg4UtUHvlUHTyZvtP1nC2xuSrDqn1/OT5OmJDoPgRpOkZcbF2dh5q1MtoMu63Sa9Oqvhzj4jLLXaCwdB04t89/1O/w1cDnyilFU=')
    try:
        # 網址被執行時，等同使用 GET 方法發送 request，觸發 LINE Message API 的 push_message 方法
        line_bot_api.push_message('U9c2394cb40e9cc5c619de3b1eddcee96',TextSendMessage(text="歡迎使用DOG"))
        #針對user ID 去發佈文字訊息
        return 'ok'
    except:
        print('error')
        
if __name__=="__main__":
    run_with_ngrok(app)
    app.run()