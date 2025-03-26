import requests
from bs4 import BeautifulSoup
from linebot.v3.messaging import MessagingApi, Configuration, ApiClient
from linebot.v3.messaging.models import TextMessage, ImageMessage, PushMessageRequest

# 在這裡填入你的 LINE Channel Access Token
LINE_CHANNEL_ACCESS_TOKEN = '__你的token__'

# 設定 API 配置
config = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)

# 建立 API 用戶端
api_client = ApiClient(configuration=config)

# 初始化 Messaging API
messaging_api = MessagingApi(api_client)

# 使用者 ID
user_id = '__你的UserID__'

# 目標網址
url = "https://tw.news.yahoo.com/archive/"

# 發送請求
response = requests.get(url)

# 確保請求成功
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 找到新聞的部分（調整選擇器以符合最新的 Yahoo 頁面結構）
    articles = soup.find_all('div', class_='Cf')[:5]  # 假設新聞項目在 div 中

    # 遍歷前五個新聞並發送
    for i, article in enumerate(articles):
        # 取得新聞標題
        title_tag = article.find('h3')
        if title_tag:
            title = title_tag.get_text()

            # 取得新聞連結
            link_tag = article.find('a')
            if link_tag and 'href' in link_tag.attrs:
                full_link = f"https://tw.news.yahoo.com{link_tag['href']}"
            else:
                full_link = "無法取得連結"

            # 取得新聞封面圖片
            image_tag = article.find('img')
            if image_tag and 'src' in image_tag.attrs:
                img_src = image_tag['src']
            else:
                img_src = "No image available"

            # 組合新聞資訊訊息
            news_info = f'新聞標題：{title}\n連結：{full_link}'

            # 打印新聞標題、連結和封面圖片 URL
            """print(f"新聞標題：{title}")
            print(f"連結：{full_link}")
            print(f"封面圖片：{img_src}\n")"""

            # 建立推送文字訊息請求
            text_message_request = PushMessageRequest(
                to=user_id,
                messages=[TextMessage(text=news_info)]
            )

            # 發送文字訊息
            messaging_api.push_message(text_message_request)

            # 如果有封面圖片，建立圖片訊息請求
            if img_src != "No image available":
                image_message_request = PushMessageRequest(
                    to=user_id,
                    messages=[ImageMessage(original_content_url=img_src, preview_image_url=img_src)]
                )

                # 發送圖片訊息
                messaging_api.push_message(image_message_request)
else:
    print(f"無法抓取資料，狀態碼: {response.status_code}")
