import requests
'''
    向requests.get 请求中传递参数。
'''

url = 'https://movie.douban.com/j/chart/top_list'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        }
param = {
    "type": '11',
    "interval_id": "100:90",
    "action":"",
    "start": "0",
    "limit": "20",
}

resp = requests.get(url,headers=headers,params=param)
print(resp.json())
resp.close()   #关闭请求