import requests
from bs4 import BeautifulSoup
from linebot.v3.messaging import MessagingApi, Configuration, ApiClient
from linebot.v3.messaging.models import TextMessage, PushMessageRequest

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

# 目標網址 (PTT 棒球版)
url = "https://www.ptt.cc/bbs/Baseball/index.html"

# 設定 cookies 來跳過 PTT 18 歲驗證
cookies = {'over18': '1'}

# 發送請求
response = requests.get(url, cookies=cookies)

# 確保請求成功
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到文章的標題區塊
    articles = soup.find_all('div', class_='title')[:10]  # 抓取前 10 篇文章

    # 遍歷前 10 篇文章並發送
    for i, article in enumerate(articles):
        # 取得文章標題
        if article.a:
            title = article.a.text.strip()

            # 取得文章連結
            link = f"https://www.ptt.cc{article.a['href']}"

            # 組合文章資訊訊息
            post_info = f'{i+1}\n文章標題：{title}\n連結：{link}'

            # 打印文章標題和連結
            print(f"文章標題：{title}")
            print(f"連結：{link}\n")

            # 建立推送文字訊息請求
            text_message_request = PushMessageRequest(
                to=user_id,
                messages=[TextMessage(text=post_info)]
            )

            # 發送文字訊息
            messaging_api.push_message(text_message_request)
else:
    print(f"無法抓取資料，狀態碼: {response.status_code}")
