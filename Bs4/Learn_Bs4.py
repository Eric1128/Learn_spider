import requests
from bs4 import BeautifulSoup as BS    #安装  pip install bs4

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        }
f_url = "https://dytt89.com/"
resp = requests.get(f_url,headers=headers,verify=False)   #verify=False 去掉安全验证
resp.encoding='gb2312'     # 指定字符集
html_ydm = resp.text
resp.close()

#1、把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BS(html_ydm,"html.parser")    #bs4截图解析很多类型的数据，所以需要指定数据类型： “html.parser” 指定html解析器
#2、从bs对象中查找数据
    # find(标签，属性=指)  查找一个数据
    # find_all(标签，属性=指) 查找所有数据
#data = page.find("div",class_="co_content222")   # <div class="co_content222">  因为class 在python中是关键字，所以需要使用class_进行区分
data = page.find('div',attrs={"class":"co_content222"})  # 与上一行的表达意思一致。
li_list = data.find_all('li')[1:]
url_list = []
for li in li_list:
    url1 = li.find('a').get('href')   #通过get 可以直接拿到标签中的属性值
    url_list.append(f_url.strip('/')+url1)    #将连接装填到rul_list 中

#循环子页面Url 列表，进子页面请求
for child_url in url_list:
    child_resp = requests.get(child_url,headers=headers,verify=False)
    child_resp.encoding = 'gb2312'
    child_text = child_resp.text
    child_resp.close()

    #页面源代码导入 BeautifulSoup 进行处理
    child_page = BS(child_text,"html.parser")
    img_url = child_page.find("div",attrs={"id":"Zoom"}).find('img').get('src')   #获取到 img的URL
    img_name = img_url.split('/')[-1]

    #下载图片
    img_resp = requests.get(img_url)

    #保存图片   注：pycharm默认会给每个文件加载索引，如果下载图片太多会导致pycharm特别卡，通过文件夹img 右键--》Mark Directory AS --> Exclusion 来关闭创建文件索引
    f = open('img/'+img_name,mode='wb')
    f.write(img_resp.content)    #通过img_resp.content 可以拿到图片的字节
    f.close()
    print('over-->',img_name)
print("all over ！！！！")