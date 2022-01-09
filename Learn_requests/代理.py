#做一个笔记，但是不建议使用代理
import requests

proxies = {
  "http": "http://10.10.1.10:80",
  "https": "http://10.10.1.10:1080",
}
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        }

resp = requests.get("http://12345678.html",proxies = proxies,headers=headers)
resp.encoding = 'utf-8'
print(resp.text)