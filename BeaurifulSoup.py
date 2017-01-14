
from bs4 import BeautifulSoup

html = '\
<html>\
    <body>\
        <h1 id=\'title\'>Hello World</h1>\
        <a href="#" class ="link">This is link1</a>\
        <a href="#" class ="link">This is link2</a>\
    </body>\
</html>\
'

soup = BeautifulSoup(html,"html.parser")
print(soup.text)                    #把不含標籤(tag)的資訊全部抽取出來，所以會印出 Hello World This is link1 This is link2
print(type(soup.text))              #印出 <class 'str'>
print(soup.contents)                #傳出一個list物件，裡面的元素為包含標籤(tag)的Tag物件          [<html> <body> <h1 id="title">Hello World</h1> <a class="link" href="#">This is link1</a> <a class="link" href="#">This is link2</a> </body></html>]
print(type(soup.contents[0]))       #印出<class 'bs4.element.Tag'>
print(soup.select('body'))          #印出一個list物件，裡面的元素是指定標籤內包含的Tag物件      [<body> <h1 id="title">Hello World</h1> <a class="link" href="#">This is link1</a> <a class="link" href="#">This is link2</a> </body>]
print(type(soup.select('body')[0])) #印出<class 'bs4.element.Tag'>    所以 soup.select('body')[0] 不是str物件
print(soup.select('body')[0].text)  #印出  Hello World This is link1 This is link2  這是一個str物件
print(soup.select('a'))              #印出一個list物件，裡面的元素是指定標籤內包含的Tag物件      [<a class="link" href="#">This is link1</a>, <a class="link" href="#">This is link2</a>]
print(soup.select('#title'))          #印出一個list物件，裡面的元素是指定id內包含的Tag物件           [<h1 id="title">Hello World</h1>]
print(soup.select('.link'))           #印出一個list物件，裡面的元素是指定class內包含的字串            [<a class="link" href="#">This is link1</a>, <a class="link" href="#">This is link2</a>]

