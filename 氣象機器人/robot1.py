# 建立了一個 reply_image 函式，使用 requests 的 GET 方法傳送圖片。
# 因為傳送訊息時需要 access token 和 reply token，所以將這兩個值變成 reply_message 函式的參數。
# 將 access token 和 channel_secret 獨立為變數。
# 使用 if 判斷訊息是否出現「雷達回波圖」或「雷達回波」。
# 使用標準函式庫 time 來增加圖片的時間戳記。

from inspect import signature
from flask_ngrok import run_with_ngrok
from flask import Flask , request

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi,WebhookHandler
from linebot.models import MessageEvent,TextMessage,TextSendMessage

# 載入 json 標準函式庫，處理回傳的資料格式
import requests,json,time

app=Flask(__name__)

access_token='+JAdt9yX+wmgrfIzy56ZWeB1x6k+qcD8NRnRVSvjQ8r92biHmdSNX+dsBL6K2Y3vU+yXeHjDwwRSfFF+JhsKJ42L6gN+XIUQJv+TI/E8/tO1ny4mKXpM7SI8BVx/fsFcrdrsaNBlV8Sq0DljuMwHlQdB04t89/1O/w1cDnyilFU='
channel_secret='cf112f08117acf6fdea82505d75e567c'

@app.route("/",methods=['POST'])
def linebot():
    body=request.get_data(as_text=True)
    try:
        line_bot_api=LineBotApi(access_token)
        handler=WebhookHandler(channel_secret)
        signature=request.headers['X-Line-Signature']
        handler.handle(body,signature)
        json_data=json.loads(body)
        reply_token=json_data['events'][0]['replyToken']
        user_id=json_data['events'][0]['source']['userId']
        print(json_data)
        if 'message' in json_data['events'][0]:       #如果傳送是message
            if json_data['events'][0]['message']['type']=='text':  # 如果message的類別是text
                text=json_data['events'][0]['message']['text']     #取出text內容
                if text=='雷達回波圖' or text=='雷達回波' :          # 如果是雷達回波圖相關的文字
                    # 傳送雷達回波圖 ( 加上時間戳記 )
                    reply_image(f'https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}', reply_token, access_token)
                else:
                    # 如果是一般文字，直接回覆同樣的文字 
                    reply_message(text,reply_token,access_token)
    except:
        print("error")    # 如果發生錯誤，印出 error
    return 'Ok'           # 驗證 Webhook 使用，不能省略

if __name__=="__main__":  # 串連 ngrok 服務
    run_with_ngrok(app)
    app.run()

# LINE 回傳圖片函式
def reply_image(msg,rk,token):
    headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'}
    body={
        'replyToken':rk,
        'messages':[{
            'type':'image',
            'originalContentUrl':msg,    #originalContentUrl 是使用者點開之後出現的圖片
            'previewImageUrl':msg        #previewImageUrl 是預覽圖
        }]
    }
    req=requests.request('POST','https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(body).encode('utf-8'))
    print(req.text)

# LINE 回傳訊息函式
def reply_message(msg,rk,token):
    headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'}
    body={
        'replyToken':rk,
        'messages':[{
            "type":"text",
            "text":msg
        }]
    }
    req=requests.request('POST','https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(body).encode('utf-8'))
    print(req.text)