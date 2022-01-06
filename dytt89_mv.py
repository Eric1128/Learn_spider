import requests
import re
import csv

f = open('dytt_date.csv',mode='a',encoding='utf8')
csv_w = csv.writer(f)

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        }
f_url = "https://dytt89.com/"
resp = requests.get(f_url,headers=headers,verify=False)   #verify=False 去掉安全验证
resp.encoding='gb2312'     # 指定字符集

html_ydm = resp.text
obj = re.compile(r'2021必看热片.*?<ul>(?P<li>.*?)</ul>',re.S)
obj1 = re.compile(r"<a href='(?P<sub_url>.*?)'",re.S)
obj3 = re.compile(r'◎译　　名　(?P<yiming>.*?)<br />'
                  r'◎片　　名　(?P<movie>.*?)<br />.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)
result = obj.finditer(html_ydm)
child_url_list = []
for it in result:
    li_ydm = it.group('li')

    url_result = obj1.finditer(li_ydm)
    for url in url_result:
        url1 = f_url.strip("/")+url.group("sub_url")
        child_url_list.append(url1)


for u in child_url_list:
    child_resp = requests.get(u,headers=headers,verify=False)
    child_resp.encoding = 'gb2312'
    child_ydm = child_resp.text
    child_result = obj3.search(child_ydm)
    dic = child_result.groupdict()
    csv_w.writerow(dic.values())

f.close()
print('over')
