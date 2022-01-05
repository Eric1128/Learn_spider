import requests
import re
import csv

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        }
f = open("douban_mv_top250.csv",mode='a',encoding="utf8")
csv_w = csv.writer(f)
i = 0
while i<250:
    url = "https://movie.douban.com/top250?start={}&filter=".format(i)
    i += 25
    resp = requests.get(url,headers=headers)
    html_ydm = resp.text
    obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?'
                      r'<p class="">.*?br>(?P<year>.*?)&nbsp;.*?'
                      r'<span class="rating_num" property="v:average">(?P<pcore>.*?)</span>.*?'
                      r'<span>(?P<num>.*?)人评价</span>',re.S)
    result = obj.finditer(html_ydm)
    for it in result:
    #     print(it.group("name"))
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()+"年"
        dic['num'] = dic['num'].strip()+"人评论"
        dic['pcore'] = dic['pcore'].strip()+"分"
        csv_w.writerow(dic.values())
f.close()
print("over")
