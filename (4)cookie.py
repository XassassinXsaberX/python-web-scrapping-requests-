import requests
import webbrowser

headers = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0' ,
            'Referer':"http://www.pixiv.net"
        }
#利用google的開發人員工具來觀察我們pixiv這個網頁上的cookie (為一個字串)
cookies = 'p_ab_id=5; login_ever=yes; a_type=0; is_sensei_service_user=1; __utmt=1; _gat=1; _gat_UA-74360115-3=1; PHPSESSID=22133271_6a0ba3a49bd01727af70796d9a84d0b5; device_token=2cdcf3f6de96716783e4d444a675faab; module_orders_mypage=%5B%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; __utma=235335808.623028923.1484053960.1484053960.1484053960.1; __utmb=235335808.13.10.1484053960; __utmc=235335808; __utmz=235335808.1484053960.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=22133271=1; _ga=GA1.2.623028923.1484053960; ki_t=1484054051140%3B1484054051140%3B1484055392110%3B1%3B7; ki_r='

#用requests套件建立get方法的連線時，對於傳遞cookie有兩種方法
#一種是使用requests.cookies.RequestsCookieJar 建立實例，另一種是用dict物件

#法一
jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)

#法二
lt = cookies.split(';')
s = dict()
for i in range(len(lt)):
    s[lt[i].split('=')[0]] = lt[i].split('=')[1]

req = requests.get("http://www.pixiv.net",cookies = s, headers=headers)                           #如果建立連線時不放入cookie，就會無法登入，因為這個cookie已經儲存了我們登入的資訊了
req = requests.get("http://www.pixiv.net/ranking.php?mode=daily&content=illust",headers=headers)  #該連線時不放入cookie，仍可進行(只不過仍沒有登入)

print(req.text)



