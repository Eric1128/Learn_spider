import requests

while True:
    url = 'https://fanyi.baidu.com/sug'
    kw = input("请输入要翻译的英文：")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        }
    data = {
        "kw":kw
    }
    resp = requests.post(url,data=data,headers=headers)

    for item in resp.json()['data']:
        print(item['k'],':',item['v'])
    resp.close()