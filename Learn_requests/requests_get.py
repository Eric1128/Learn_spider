import requests

name = input("请输入一个明星：")
url = 'https://www.sogou.com/web?query={}'.format(name)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

resp = requests.get(url,headers=headers)
print(resp.text)

resp.close()    # 关闭请求连接