#通过session 保存回话cookie.
# 1、通过账号密码登录，获取cookie
# 2、通过cookie 获取想要的数据
import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        }

url = 'https://passport.17k.com/ck/user/login'
#构造session 会话
session = requests.session()
data={
    "loginName": "13522755117",
    "password": "1234@qwer"
}

#登录，获取cookie
resp = session.post(url,headers=headers,data=data)
# print(resp.text)   #打印登录后的返回值
# print(resp.cookies)  #打印返回的cookies

#获取我看过的书：https://user.17k.com/www/bookshelf/read.html，发现此页面的源代码中没有数据。查找数据来源
mybook_url = 'https://user.17k.com/ck/user/mine/readList?page=1&appKey=2406394919'    #数据在json中
book_resp = session.get(mybook_url,headers=headers)    #获取数据
session.close()     #关闭会话
# print(book_resp.json()['data'])      #查看 原数据
for book in book_resp.json()['data']:
    bookName = book['bookName']
    coverImg = book['coverImg']
    authorPenName = book['authorPenName']
    bookClass = book['bookClass']['name']
    print(bookClass,"\t",bookName,"\t",coverImg,"\t",authorPenName)