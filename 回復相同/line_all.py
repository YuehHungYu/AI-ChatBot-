from flask import Flask,request
from flask_ngrok import run_with_ngrok
from linebot import LineBotApi,WebhookHandler
from linebot.models import TextSendMessage,ImageSendMessage,LocationSendMessage,StickerSendMessage
import json

app=Flask(__name__)

@app.route("/",methods=['POST'])
# 建立路由與對應的處理函式
# 使用 app.route(routepath) 這個裝飾氣(decorator)來為你的路徑設定服務的function。
# 在首頁使用POST方式傳送參數

def linebot():
    body=request.get_data(as_text=True)
    json_data=json.loads(body)
    print(json_data)
    try:
        line_bot_api=LineBotApi('TeQd4PjfhKAOszYj30cvcBWwGlEcngP1cZh3y3uFAt8lOuqBwUhX39hNpP5J7PMbxYvqG9QEQg4UtUHvlUHTyZvtP1nC2xuSrDqn1/OT5OmJDoPgRpOkZcbF2dh5q1MtoMu63Sa9Oqvhzj4jLLXaCwdB04t89/1O/w1cDnyilFU=')
        handler=WebhookHandler('2c70b7d37347804b9d7806ae44040598')
        signature=request.headers['X-Line-Signature']
        handler.handle(body,signature)
        tk=json_data['events'][0]['replyToken']
        tp=json_data['events'][0]['message']['type']
        
        if tp=="text":
            msg=reply_msg(json_data['events'][0]['message']['text'])
            if msg[0]=='text':
                # 如果要回傳的訊息是 text，使用 TextSendMessage 方法
                line_bot_api.reply_message(tk,TextSendMessage(text=msg[1]))
            if msg[0]=='location':
                # 如果要回傳的訊息是 location，使用 LocationSendMessage 方法
                line_bot_api.reply_message(tk,LocationSendMessage(title=msg[1]['title'],
                                                                    address=msg[1]['address'],
                                                                    latitude=msg[1]['latitude'],
                                                                    longitude=msg[1]['longitude']))
            if msg[0]=='image':
                # 如果要回傳的訊息是 image，使用 ImageSendMessage 方法
                line_bot_api.reply_message(tk,ImageSendMessage(original_content_url=msg[1],
                                                                preview_image_url=msg[1]))
        
        if tp=="sticker":
            stickerID=json_data['events'][0]['message']['stickerId']
            # 取得 stickerId
            packageID=json_data['events'][0]['message']['packageId']
            # 取得 packageID
            sticker_msg=StickerSendMessage(sticker_id=stickerID, package_id=packageID)
            # 設定回傳同樣的訊息
            line_bot_api.reply_message(tk,sticker_msg)
        
        if tp == 'location':
            # 如果是收到的訊息是地點資訊
            line_bot_api.reply_message(tk,TextSendMessage(text='好地點！'))
        if tp == 'image':
            # 如果是收到的訊息是圖片
            line_bot_api.reply_message(tk,TextSendMessage(text='好圖給讚！'))
        if tp == 'audio':
            # 如果是收到的訊息是聲音
            line_bot_api.reply_message(tk,TextSendMessage(text='聲音讚喔～'))
        if tp == 'video':
            # 如果是收到的訊息是影片
            line_bot_api.reply_message(tk,TextSendMessage(text='影片內容真是不錯！'))
    except:
        print("error")
    return 'ok'

# 定義回覆訊息的函式
# 增加回復資訊量 #TODO
def reply_msg(text):
    msg_dict = {
        'hi':'Hi! 你好呀～',
        'hello':'Hello World!!!!',
        '你好':'你好呦～',
        'help':'有什麼要幫忙的嗎？'
    }
    # 如果出現特定地點，提供地點資訊
    local_dict = {
        '總統府':{
            'title':'總統府',
            'address':'100台北市中正區重慶南路一段122號',
            'latitude':'25.040319874750914',
            'longitude':'121.51162883484746'
        },
        '101':{
            'title':'台北 101',
            'address':'110台北市信義區信義路五段7號',
            'latitude':'25.034095712145003',
            'longitude':'121.56489941996108'
            }
    }
    # 如果出現特定圖片文字，提供圖片網址
    img_dict = {
        '皮卡丘':'https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png',
        '傑尼龜':'https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png'
    }
    # 預設回覆的文字就是收到的訊息
    reply_msg_content = ['text',text]
    if text in msg_dict:
        reply_msg_content = ['text',msg_dict[text.lower()]]
    if text in local_dict:
        reply_msg_content = ['location',local_dict[text.lower()]]
    if text in img_dict:
        reply_msg_content = ['image',img_dict[text.lower()]]
    return reply_msg_content

if __name__ == "__main__":
    run_with_ngrok(app)
    app.run()