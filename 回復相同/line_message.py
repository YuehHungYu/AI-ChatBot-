from flask_ngrok import run_with_ngrok
from flask import Flask,request

# 載入Line Message API 函式庫
from linebot import LineBotApi,WebhookHandler
from linebot.models import TextSendMessage

# 載入Json 標準函式庫，處理回傳資料格式
import json

# 回傳相同訊息
#  'events': [{'type': 'message', 
#                 'message': {'type': 'text',  
#                             'text': '你好'}, 


app=Flask(__name__)

@app.route("/",methods=['POST'])
def linebot():
    body=request.get_data(as_text=True)
    #取得收到的訊息內容
    json_data=json.loads(body)
    # JSON格式化訊息內容
    print(json_data)
    try:
        access_token='TeQd4PjfhKAOszYj30cvcBWwGlEcngP1cZh3y3uFAt8lOuqBwUhX39hNpP5J7PMbxYvqG9QEQg4UtUHvlUHTyZvtP1nC2xuSrDqn1/OT5OmJDoPgRpOkZcbF2dh5q1MtoMu63Sa9Oqvhzj4jLLXaCwdB04t89/1O/w1cDnyilFU='
        secret='2c70b7d37347804b9d7806ae44040598'
        line_bot_api=LineBotApi(access_token)
        # 確認token是否正確
        handler=WebhookHandler(secret)
        # 確認secret是否正確
        signature=request.headers['X-Line-Signature']
        # 加入回傳的headers
        handler.handle(body,signature)
        # 綁定訊息回傳的相關資訊
        
        
        msg=json_data['events'][0]['message']['text']
        # 取得用戶輸入的資訊
        tk=json_data['events'][0]['replyToken']
        # 取得replyToken 
        text_msg=TextSendMessage(text=msg)
        # 設定回傳同樣的訊息
        line_bot_api.reply_message(tk,text_msg)
        # 回傳訊息
        # print(msg,tk)
    except:
        print('error')
    return 'ok'

if __name__=="__main__":
    run_with_ngrok(app)
    app.run()