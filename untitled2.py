import requests
from bs4 import BeautifulSoup
import os
import threading


    

def get_photolist(photo_name, download_num):    
    page = 1     #初始頁數為1
    photo_list = []     #建立空的圖片 list
    
    while True:
       url = 'http://www.dils.tku.edu.tw/dilswordpress/%E7%B3%BB%E6%89%80%E4%BB%8B%E7%B4%B9/%E5%B8%AB%E8%B3%87%E9%99%A3%E5%AE%B9/'
      #設定連結
       html = requests.get(url)     #GET請求
       html.encoding = 'utf-8'     #指定編碼為utf-8        
       bs = BeautifulSoup(html.text, 'lxml')     #解析網頁 
       print(photo_item = bs.find_all('td', {'class': 'column-1'}[0].href))     
        #尋找所有標籤為 td, calss 為 'coiumn-1' 的元素 

#print(bs.find_all('td', {'class': 'column-1'})[1]['class'])
            
#print(bs.find_all('img', {'width': '130'})[0]['src'])

result = bs.find_all('img', {'width': '130'})[0]['src']


