#會話(session)物件
#在第一個範例的請求中，每次請求其實都相當於發起了一個新的請求。
# 也就是相當於我們每個請求都用了不同的瀏覽器單獨打開的效果。
# 也就是它並不是指的一個會話，即使請求的是同一個網址。


#會話維持
#在requests中，我們如果直接利用requests.get()或requests.post()等方法的確可以做到模擬網頁的請求。但是這實際上是相當於不同的會話，即不同的session，也就是說相當於你用了兩個瀏覽器打開了不同的頁面。
#設想這樣一個場景，你第一個請求利用了requests.post()方法登錄了某個網站，第二次想獲取成功登錄後的自己的個人信息，你又用了一次requests.get()方法。實際上，這相當於打開了兩個瀏覽器，是兩個完全不相關的會話，你說你能成功獲取個人信息嗎？那當然不能。
#有小伙伴就說了，我在兩次請求的時候都設置好一樣的Cookie不就行了？行是行，但是不覺得麻煩嗎？每次都要這樣。是我我忍不了。
#其實解決這個問題的主要方法就是維持同一個會話，也就是相當於打開一個新的瀏覽器選項卡而不是新開一個瀏覽器。但是我又不想每次設置Cookie，那該怎麼辦？這時候就有了新的利器Session。
#利用它，我們可以方便地維護一個會話，而且不用擔心Cookie的問題，它會幫我們自動處理好。

import requests

requests.get("http://httpbin.org/cookies/set/sessioncookie/123456789")
r = requests.get("http://httpbin.org/cookies")
print(r.text)


#很明顯，這不在一個會話中，無法獲取cookies，那麼在一些站點中，我們需要保持一個持久的會話怎麼辦呢？
# 就像用一個瀏覽器逛淘寶一樣，在不同的選項卡之間跳轉，這樣其實就是建立了一個長久會話。
#解決方案如下
s = requests.session()                                       #建立一個session object
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)