#參考網站
#https://www.youtube.com/watch?v=G5MDpnGsE-k&list=PLohb4k71XnPaQRTvKW4Uii1oq-JPGpwWF&index=15      建立一個session實例，並利用他來post 表單來進入八卦板
#http://violin-tao.blogspot.tw/2015/05/python-part-5-cookie-firefoxcookie.html                                                                利用cookie進入八卦板
import requests
from bs4 import BeautifulSoup

value = {'from':'/bbs/Gossiping/index.htmnl','yes':'yes'}

rs = requests.session()                                                  #會話物件讓你能夠跨請求保持某些參數。它也會在同一個Session實例發出的所有請求之間保持cookie，期間使用urllib3的connection pooling功能。
                                                                         #所以如果你向同一主機發送多個請求，底層的TCP連接將會被重用，從而帶來顯著的性能提升。(參見HTTP persistent connection ).
                                                                         #HTTP持久連線（HTTP persistent connection，也稱作HTTP keep-alive或HTTP connection reuse）是使用同一個TCP連線來傳送和接收多個HTTP請求/應答，
                                                                         # 而不是為每一個新的請求/應答開啟新的連線的方法。

res = rs.post("https://www.ptt.cc/ask/over18",verify=True,data=value)     #利用post方法，來送出表單
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html',verify=True)     # 現在隨處可見https 開頭的網站，Requests可以為HTTPS請求驗證SSL憑證，就像web瀏覽器一樣。要想檢查某個主機的SSL憑證，你可以使用verify 參數


#另一種是採用cookie的方法
res1 = requests.get("https://www.ptt.cc/bbs/Gossiping/index.html",cookies={"over18":"1"})
#print(res1.text)

