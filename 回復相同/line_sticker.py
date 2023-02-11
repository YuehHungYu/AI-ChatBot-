from flask_ngrok import run_with_ngrok
from flask import Flask,request
from linebot import LineBotApi,WebhookHandler
from linebot.models import StickerSendMessage
import json

# 回覆表情貼圖
# 'events': [{'type': 'message', 
#                 'message': {'type': 'sticker',  
#                             'stickerId': '52114112'}, 


app=Flask(__name__)
@app.route("/",methods=['POST'])
# 在首頁使用POST方式傳送參數
# 使用 @app.route(routepath) 這個裝飾氣(decorator)來為你的路徑設定服務的function。
# 建立路由與對應的處理函式

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
        # get X-Line-Signature header value
        # 取得 Request Header 中的 X-Line-Signature 來比對 signature 這個值就行，
        # 二者相同就代表確認是透過 LINE 發來的
        
        handler.handle(body,signature)
        # 綁定訊息回傳的相關資訊
        # 幫你判斷要用剛剛設定的哪個 event 來作回應
        
        
        stickerID=json_data['events'][0]['message']['stickerId']
        # 取得 stickerId
        packageID=json_data['events'][0]['message']['packageId']
        # 取得 packageID
        tk=json_data['events'][0]['replyToken']
        # 取得replyToken 
        sticker_msg=StickerSendMessage(sticker_id=stickerID, package_id=packageID)
        # 設定回傳同樣的訊息
        line_bot_api.reply_message(tk,sticker_msg)
        # 回傳訊息
        # print(msg,tk)
    except:
        print('error')
    return 'ok'

if __name__=="__main__":
    run_with_ngrok(app)
    app.run()