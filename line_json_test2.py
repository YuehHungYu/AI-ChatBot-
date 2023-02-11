from cgitb import handler
from inspect import signature
from flask_ngrok import  run_with_ngrok
from flask import Flask,request

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi,WebhookHandler
from linebot.models import  MessageEvent,TextMessage,TextSendMessage

# 載入 json 標準函式庫，處理回傳的資料格式
import json


app=Flask(__name__)
line_bot_api=LineBotApi('+JAdt9yX+wmgrfIzy56ZWeB1x6k+qcD8NRnRVSvjQ8r92biHmdSNX+dsBL6K2Y3vU+yXeHjDwwRSfFF+JhsKJ42L6gN+XIUQJv+TI/E8/tO1ny4mKXpM7SI8BVx/fsFcrdrsaNBlV8Sq0DljuMwHlQdB04t89/1O/w1cDnyilFU=')
handler=WebhookHandler('cf112f08117acf6fdea82505d75e567c')

@app.route("/",methods=['POST'])
def linebot():
    body=request.get_data(as_text=True)    # 取得收到的訊息內容
    try:
        signature=request.headers['X-Line-Signature']    # 加入回傳的 headers
        handler.handle(body,signature)     # 綁定訊息回傳的相關資訊
        json_data=json.loads(body)
        print(json_data)
    except:
        print("error")
    return 'ok'
if __name__ =="__main__":
    run_with_ngrok(app)
    app.run()