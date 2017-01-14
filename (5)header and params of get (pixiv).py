import requests

#送出一個get請求，並附加參數上去
webheader = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}
payload = {'s_mode':'s_tag','word':'fate',"order":'data_d','p':'12'}
r = requests.get("http://www.pixiv.net/search.php",params=payload,headers=webheader)      #在pixiv中按下搜尋時，實際上是利用get方法送出request，其後還會加上一些參數   (需要用網頁開發人員工具來觀察)
                                                                                         #所以以上是代表在pixiv網站中搜尋fate  然後時間從新到舊排序  第12頁的搜尋結果
print(r.url)                                                                             #印出 http://www.pixiv.net/search.php?word=fate&p=12&order=data_d

#某些網站反感爬蟲的到訪，於是對爬蟲一律拒絕請求。所以用直接訪問網站經常會出現HTTP Error 403: Forbidden的情況
#對有些header要特別留意，Server端會針對這些header做檢查
#1.User-Agent有些Server或Proxy會檢查該值，用來判斷是否是瀏覽器發起的Request
#2.Content-Type在使用REST接口時，Server會檢查該值，用來確定HTTP Body中的內容該怎樣解析。
#
#
#通過header讓requests的程序去偽裝瀏覽器，或者該網頁的環境，可以有效避免服務器拒絕和跨域限制。

#另外，我們還有對付”反盜鏈”的方式，對付防盜鏈，服務器會識別headers中的Referer是不是它自己，
# 如果不是，有的服務器不會響應，所以我們還可以在headers中加入referer
webheader = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0' ,
              'Referer':"http://www.pixiv.net/member_illust.php?mode=medium&illust_id=60573544"
              }

#使用我的cookie
cookies = 'p_ab_id=5; login_ever=yes; a_type=0; is_sensei_service_user=1; __utmt=1; _gat=1; _gat_UA-74360115-3=1; PHPSESSID=22133271_6a0ba3a49bd01727af70796d9a84d0b5; device_token=2cdcf3f6de96716783e4d444a675faab; module_orders_mypage=%5B%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; __utma=235335808.623028923.1484053960.1484053960.1484053960.1; __utmb=235335808.13.10.1484053960; __utmc=235335808; __utmz=235335808.1484053960.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=22133271=1; _ga=GA1.2.623028923.1484053960; ki_t=1484054051140%3B1484054051140%3B1484055392110%3B1%3B7; ki_r='
lt = cookies.split(';')
s = dict()
for i in range(len(lt)):
    s[lt[i].split('=')[0]] = lt[i].split('=')[1]

#或著提交表單來login
#至於方法我這裡就不列了，請見 post(login to pixiv).py

r = requests.get("http://www.pixiv.net/member_illust.php?mode=medium&illust_id=60573544",headers = webheader,cookies = s)
print(r.text)          #我們可以在文中發現一個原圖的url    http://i1.pixiv.net/img-original/img/2016/12/26/18/14/27/60573544_p0.jpg
r = requests.get("http://i1.pixiv.net/img-original/img/2016/12/26/18/14/27/60573544_p0.jpg",headers=webheader)
print(r.status_code)
with open("picture.jpg","wb") as f:
    f.write(r.content)
#順利下載該圖片了


