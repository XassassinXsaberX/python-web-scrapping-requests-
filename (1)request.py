import requests
from bs4 import BeautifulSoup

res = requests.get("http://www.douban.com/")
print(res.text)         #印出網頁的html原始碼，為str的字串
print(res.content)      #印出網頁的html byte原始碼(所以這個資料也可以直接寫入到本機檔案中，可用來下載檔案)
print(res.encoding)     #印出網頁的編碼方式  utf-8  (如果是圖片的話會顯示None，因為圖片不是文字檔，而是二進位檔)
print(res.status_code)  #印出 HTTP status code
print(res.cookies)      #印出cookie資訊
print(res.url)          #印出 https://www.douban.com/

#requests 模組也提供了http所有的基本 request 方法
r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")


