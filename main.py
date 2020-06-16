import requests
from bs4 import BeautifulSoup
import os          #新建及管理資料夾&檔案
import threading   #用多執行緒模組下載

Teacher = ('Teacher')
#os.mkdir(Teacher) #當檔案已存在時，無法建立該檔案。
   
url = 'http://www.dils.tku.edu.tw/dilswordpress/%E7%B3%BB%E6%89%80%E4%BB%8B%E7%B4%B9/%E5%B8%AB%E8%B3%87%E9%99%A3%E5%AE%B9/'
      #設定連結
html = requests.get(url)     #GET請求
html.encoding = 'utf-8'     #指定編碼為utf-8        
bs = BeautifulSoup(html.text, 'lxml')     #解析網頁 
#  print(photo_item = bs.find_all('td', {'class': 'column-1'}[0].href))     
        #尋找所有標籤為 td, calss 為 'coiumn-1' 的元素 

#print(bs.find_all('td', {'class': 'column-1'})[1]['class'])
            
#print(bs.find_all('img', {'width': '130'})[0]['src'])

#photo_item = bs.find_all('img', {'width': '130'})
photo_item = bs.find_all('td', {'class': 'column-1'}) 
photo_lever = bs.find_all('td', {'class': 'column-2'}) 
photo_name = bs.find_all('td', {'class': 'column-3'}) 
#print(photo_item)
photo_list = []
for i in range(len(photo_item)):
    photo = photo_item[i].find('img')['src'] #一定只能找底下的標籤，若只有一個標籤什麼都不能找，會格是錯誤。
    photo_list.append(photo)

    name = photo_name[i].text
    lever = photo_lever[i].text
    
    pic = requests.get(photo)     #使用 GET 對圖片連結發出請求
    
    path = 'Teacher' + '/' + name[4:7] + lever + photo[photo.rfind('.'):]
   # path += photo[photo.rfind('.'):] #將路徑加上圖片的副檔名   
    f = open(path,'wb')     #以指定的路徑建立一個檔案
    f.write(pic.content)     #將 HTTP Response 物件的 content寫入檔案中
    f.close()     #關閉檔案
print(photo_list)  
#print(photo_item[0].find('img')['src']) 

import tkinter as tk
#--↓建立主視窗↓--#
window = tk.Tk()     
window.geometry('840x640')   
window.title('405000315高宏安，座號24')        
#--↓Listbox 列表框↓--#
listbox = tk.Listbox(window,width=130 ,height=80,)
for i in range(len(photo_item)):
    photo = photo_item[i].find('img')['src']
    listbox.insert(tk.END, photo)
listbox.pack(side = tk.LEFT)
#--↓Scrollbar 捲動軸↓--#
sbar = tk.Scrollbar(window)     # 建立捲動軸
sbar.pack(side = tk.RIGHT, fill = tk.Y)
#--↓列表框與捲動軸的連結↓--#
sbar.config(command = listbox.yview)  
listbox.config(yscrollcommand = sbar.set)
#--↓啟動主視窗↓--#
window.mainloop()

