import requests,json
from linebot import LineBotApi,WebhookHandler
import json
import requests


headers={'Authorization':'Bearer TeQd4PjfhKAOszYj30cvcBWwGlEcngP1cZh3y3uFAt8lOuqBwUhX39hNpP5J7PMbxYvqG9QEQg4UtUHvlUHTyZvtP1nC2xuSrDqn1/OT5OmJDoPgRpOkZcbF2dh5q1MtoMu63Sa9Oqvhzj4jLLXaCwdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}

body={
    'size':{'width':2500,'height':1200},
    'selected':'true',
    'name':'ccc',
    'chatBarText':'選單C',
    'areas':[
        {
            'bounds':{'x':0,'y':0,'width':830,'height':280},
            'action':{'type':'richmenuswitch','richMenuAliasId':'aaa','data':'change-to-aaa'}    # 按鈕 A 使用 richmenuswitch
        },
        {
            'bounds':{'x':835,'y':0,'width':830,'height':640},
            'action':{'type':'richmenuswitch','richMenuAliasId':'bbb','data':'change-to-bbb'}    # 按鈕 B 使用 richmenuswitch
        },
        {
            'bounds':{'x':1670,'y':0,'width':830,'height':640},
            'action':{'type':'postback','data':'no-data'}   # 按鈕 C 使用 postback
        },
    ]
}
req=requests.request('POST','https://api.line.me/v2/bot/richmenu',
                        headers=headers,data=json.dumps(body).encode('utf-8'))  #  json.dumps是將 Python 對象轉換為 json 字符串
print(req.text)

# Menu ID:"richmenu-519f2faf70c20675105b606a45210aa0"

line_bot_api=LineBotApi('TeQd4PjfhKAOszYj30cvcBWwGlEcngP1cZh3y3uFAt8lOuqBwUhX39hNpP5J7PMbxYvqG9QEQg4UtUHvlUHTyZvtP1nC2xuSrDqn1/OT5OmJDoPgRpOkZcbF2dh5q1MtoMu63Sa9Oqvhzj4jLLXaCwdB04t89/1O/w1cDnyilFU=')
with open('C:/Users/88691/Desktop/練習python/聊天機器人/選單/line-rich-menu-switch-demo-c.jpg','rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-519f2faf70c20675105b606a45210aa0","image/jpeg",f)


# 將圖文選單 id 和別名 Alias id 綁定
headers={'Authorization':'Bearer TeQd4PjfhKAOszYj30cvcBWwGlEcngP1cZh3y3uFAt8lOuqBwUhX39hNpP5J7PMbxYvqG9QEQg4UtUHvlUHTyZvtP1nC2xuSrDqn1/OT5OmJDoPgRpOkZcbF2dh5q1MtoMu63Sa9Oqvhzj4jLLXaCwdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}
body={
    "richMenuAliasId":"ccc",
    "richMenuId":"richmenu-519f2faf70c20675105b606a45210aa0"
}
req=requests.request('POST','https://api.line.me/v2/bot/richmenu/alias',
                        headers=headers,data=json.dumps(body).encode('utf-8'))  #  json.dumps是將 Python 對象轉換為 json 字符串
print(req.text)


# 將圖文選單傳送到對應的 LINE 機器人
headers={'Authorization':'Bearer TeQd4PjfhKAOszYj30cvcBWwGlEcngP1cZh3y3uFAt8lOuqBwUhX39hNpP5J7PMbxYvqG9QEQg4UtUHvlUHTyZvtP1nC2xuSrDqn1/OT5OmJDoPgRpOkZcbF2dh5q1MtoMu63Sa9Oqvhzj4jLLXaCwdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}
req=requests.request("POST",'https://api.line.me/v2/bot/user/all/richmenu/richmenu-519f2faf70c20675105b606a45210aa0', headers=headers)
print(req.text)