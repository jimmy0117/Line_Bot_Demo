import requests
webhook_key = "填入Webhook金鑰"
trigger_name = "填入觸發條件名稱"
url ='https://maker.ifttt.com/trigger/'+trigger_name+'/with/key/'+webhook_key+'?value1=hello world'
requests.get(url)
