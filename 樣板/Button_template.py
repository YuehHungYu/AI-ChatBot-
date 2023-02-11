from linebot import LineBotApi,WebhookHandler
from linebot.models import PostbackAction,URIAction,MessageAction,TemplateSendMessage,ButtonsTemplate

line_bot_api=LineBotApi("TeQd4PjfhKAOszYj30cvcBWwGlEcngP1cZh3y3uFAt8lOuqBwUhX39hNpP5J7PMbxYvqG9QEQg4UtUHvlUHTyZvtP1nC2xuSrDqn1/OT5OmJDoPgRpOkZcbF2dh5q1MtoMu63Sa9Oqvhzj4jLLXaCwdB04t89/1O/w1cDnyilFU=")
line_bot_api.push_message("U9c2394cb40e9cc5c619de3b1eddcee96",TemplateSendMessage(
    alt_text='ButtonsTemplate',
    template=ButtonsTemplate(
        thumbnail_image_url="images.jpg",
        title='alan',
        text='按鈕樣板',
        actions=[
            PostbackAction(
                label='postback',
                text='發送postback'
            ),
            MessageAction(
                label="說hi!!",
                text="hi"
            ),
            URIAction(
                label="前往Google",
                uri='https://www.google.com'
            )
        ]
    )
))