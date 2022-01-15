import requests
import re
import os
'''
流程：
    1、请求页面获取M3U8文件URL
    2、请求M3U8 URL，下载M3U8文件。
    3、分析M3U8文件信息。获取视频分片 URL
    4、请求视频分片URL，并保存视屏分片
    5、使用各种手段合并视频分片，不限于开发手段
'''

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        }
url = 'https://91kanju2.com/vod-play/61399-1-1.html'
m3u8_obj = re.compile(r"url: '(?P<m3u8_url>.*?)',",re.S)     #预加载正则表达式抓取M3U8 文件

m3u8_resp = requests.get(url,headers=headers)
m3u8_url = m3u8_obj.search(m3u8_resp.text).group('m3u8_url')      #获取到M3U8的URL
m3u8_resp.close()

#请求并下载M3U8文件
download_m3u8_resp = requests.get(m3u8_url,headers=headers)
with open('mv.m3u8',mode='wb') as f:
    f.write(download_m3u8_resp.content)
download_m3u8_resp.close()
print('M3U8文件下载完毕。')

#分析处理M3U8文件，下载并保存视屏
with open('mv.m3u8',mode='r',encoding='utf-8') as f:
    n=1    #设置初始值，用于文件命名
    for line in f:
        line = line.strip()
        ts_list = []   #存放文件名的list
        if not line.startswith("#"):
            resp = requests.get(line,headers=headers)
            f1 = open('video/{}.ts'.format(n),mode='wb')
            f1.write(resp.content)
            f1.close()
            resp.close()
            print(n,'Over!!!!')
            ts_list.append("video/{}.ts".format(n))
            n += 1
        #Windows 电脑 合并视屏，代码如下:
        s = '+'.join(ts_list)
        os.system("copy /b {} aaa.mp4".format(s))     #合并视屏
        
        #MAC 电脑 合并视屏，代码如下:
        # s = ' '.join(ts_list)
        # os.system("cat {} > aaa.mp4".format(s))