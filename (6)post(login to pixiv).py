import requests
import re

webheader = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
             'Referer' : 'https: // accounts.pixiv.net / login?lang = zh_tw & source = pc & view_type = page & ref = wwwtop_accounts_index'}
data = {'pixiv_id':'a5083assassin@gmail.com',
        'password': 'ab123456789ba',
        }

url = "http://www.pixiv.net/"

r = requests.Session()
r1 = r.get("https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index",headers=webheader)

#2017.1.10 在pixiv帳號要登入用POST方法提交的表單中，除了要提交pixiv_id  password  還要提交一個 post_key 欄位的資料
#他隱藏在用get方法所得到的html原始碼中，用正規表示法來取出
lt = re.findall(r'post_key[.\W\S\w\s]+?>',r1.text)
value = lt[0].split("value=")[1]
value = value[1:-2]
data['post_key'] = value

r2 = r.post("https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index",data=data,headers=webheader)  #提交表單來登入帳號
r3 = r.get(url,headers=webheader)                                                                                                          #因為成功登入帳號，所以可以進入首頁了

#以下的方法是另外建立一個連線，然後利用剛剛登入所得到的cookie來進行登入
print(r.cookies)                                                                     #這三種cookie會不同！(第一種是我們要的)
print(r2.cookies)
print(r3.cookies)
res = requests.get(url,headers=webheader,cookies=r.cookies)                          #利用該cookie亦可連線到首頁，而不需要輸入帳號密碼來登入(同樣也成功連到首頁了)  只能用 r.cookies
#print(res.text)

