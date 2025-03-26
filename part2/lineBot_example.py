from linebot import LineBotApi
from linebot.models import TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage, VideoSendMessage
line_bot_api = LineBotApi('__你的token__')
UserID = '__你的UserID__'

#文字
text_message = TextSendMessage(text = 'hello world!')
line_bot_api.push_message(UserID, text_message)

#貼圖
Sticker_message = StickerSendMessage(package_id = '789', sticker_id = '10855')
line_bot_api.push_message(UserID, Sticker_message)

#圖片
image_message = ImageSendMessage(
    original_content_url='https://i.imgur.com/xyPtn4m.jpeg',
    preview_image_url='https://i.imgur.com/xyPtn4m.jpeg')
line_bot_api.push_message(UserID,image_message)

#位置
location_message = LocationSendMessage(
    title='CodingAPE猿創力程式設計學校',
    address='105台北市松山區延壽街374號',
    latitude=25.056434,
    longitude=121.558183)
line_bot_api.push_message(UserID,location_message)

#影片
video_message = VideoSendMessage(
    original_content_url='https://i.imgur.com/oRcIXiM.mp4',
    preview_image_url='https://i.imgur.com/xyPtn4m.jpeg'
)
line_bot_api.push_message(UserID,video_message)

#一次發多項內容時用的
# try:
# 	message = [video_message,text_message,Sticker_message,location_message,image_message]
# 	line_bot_api.push_message(UserID,message)
# except:
# 	error_message = TextSendMessage(text = '發生錯誤！')
# 	line_bot_api.push_message(UserID, error_message)


