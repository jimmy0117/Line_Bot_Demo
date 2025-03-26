import requests
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get('https://airtw.epa.gov.tw/')


select = Select(chrome.find_element(By.ID, 'ddl_county'))
select.select_by_index(1)
time.sleep(2)

date = chrome.find_element(By.CLASS_NAME, 'date')
info = date.text
info = info.split('\n')

time = info[0]
location = info[1]


airinfo = chrome.find_element(By.ID, 'aqicircle')
airinfo = airinfo.text
airinfo = airinfo.split('\n')

PM25 = airinfo[1]
condition = airinfo[2]
quality = condition + ' PM2.5 = ' + PM25
#記得更換自己的觸發條件名稱和金鑰
webhook_key = "填入Webhook金鑰"
trigger_name = "填入觸發條件名稱"
url = 'https://maker.ifttt.com/trigger/'+trigger_name+'/with/key/'+webhook_key+'?value1={}&value2={}&value3={}'.format(time, location, quality)
requests.get(url)

chrome.close()