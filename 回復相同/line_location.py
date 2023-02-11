from cgitb import handler
from inspect import signature
from flask import Flask,request
from flask_ngrok import run_with_ngrok
from linebot import LineBotApi,WebhookHandler
from linebot.models import TextSendMessage,LocationSendMessage
import json

# 回覆地址訊息
# 'events': [{'type': 'message', 'message': {'type': 'location', 
#                                            'id': '16741193533802', 
#                                            'latitude': 22.618049465301805, 
#                                            'longitude': 120.30423782765865, 
#                                            'address': '802台灣高雄市苓雅區仁智街113號'},

app=Flask(__name__)

@app.route("/",methods=['POST'])
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
        msg=json_data['events'][0]['message']['text']
        location_dect=reply_location(msg)
        if location_dect:
            # 如果有地點資訊，回傳地點
            location_message=LocationSendMessage(
                title=location_dect['title'],
                address=location_dect['address'],
                latitude=location_dect['latitude'],
                longitude=location_dect['longitude']
            )
            line_bot_api.reply_message(tk,location_message)
        else:
            # 如果是 False，回傳文字
            text_message=TextSendMessage(text="找不到")
            line_bot_api.reply_message(tk,text_message)
    except:
        print("error")
    return 'ok'
# 建立回覆地點的函式
def reply_location(text):
    # 建立地點與文字對應的字典
    location = {
        '101':{
            'title':'台北 101',
            'address':'110台北市信義區信義路五段7號',
            'latitude':'25.034095712145003',
            'longitude':'121.56489941996108'
        },
        '總統府':{
            'title':'總統府',
            'address':'100台北市中正區重慶南路一段122號',
            'latitude':'25.040319874750914',
            'longitude':'121.51162883484746'
        }
    }
    if text in location:
        return location[text]
    else:
        # 如果找不到對應的地點，回傳 False
        return False

if __name__ == "__main__":
    run_with_ngrok(app)
    app.run()