#已抓取 梨视频网站的某个视屏为例，所以直接以某个视屏URL举例
#防盗链：溯源， 需要确定本次请求的上一次请求是谁

import requests

src_url = 'https://www.pearvideo.com/video_1749325'    #在此连接的源代码中没有发现视屏的链接地址
video_id = src_url.split('_')[1]  # 获取到视屏 ID
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        #防盗链
        'Referer':src_url
        }

#在google 浏览器开发者工具中，通过刷新src_rul，发现重新请求了新的RUL，如下，并且在Request Headers 中有包含Referer 参数，因此需要在如上headers 中添加 Referer参数
# 'https://www.pearvideo.com/videoStatus.jsp?contId=1749325&mrd=0.6438576915727015'  #发下此链接的contID 和 Video_id 一致，  mrd=0.6438576915727015 此参数没用
video_url = 'https://www.pearvideo.com/videoStatus.jsp?contId={}'.format(video_id)
# video_url =f"https://www.pearvideo.com/videoStatus.jsp?contId={video_id}"  # 和上一行，意思一样

resp = requests.get(video_url,headers=headers)   #获取视屏数据json
# print(resp.json()) #查看数据,如下
'''
    {
    'resultCode': '1',
    'resultMsg': 'success',
    'reqId': '28ab30d8-2671-4a6d-98fb-e8c4b21af6fe',
    'systemTime': '1641721788164',
    'videoInfo': {
        'playSta': '1',
        'video_image': 'https://image1.pearvideo.com/cont/20220105/15898186-145307-1.png',
        'videos': {
            'hdUrl': '',
            'hdflvUrl': '',
            'sdUrl': '',
            'sdflvUrl': '',
            'srcUrl': 'https://video.pearvideo.com/mp4/third/20220105/1641721788164-15898186-145213-hd.mp4'
            }
        }
    }
'''
video_dic = resp.json()
#但是发现数据中心的 srcUrl 链接并不能打开视屏，
#'https://video.pearvideo.com/mp4/third/20220105/1641721286337-15898186-145213-hd.mp4'   #video_dic数据中的连接，打开错误
#'https://video.pearvideo.com/mp4/third/20220105/cont-1749325-15898186-145213-hd.mp4'  #开发者工具 Elements中的视频连接，可以正常观看
#对比发现并不一致，不一致的地方正好是 video_dic数据中的systemTime,因此我们提取出来进行修正
systemTime = video_dic['systemTime']
srcUrl = video_dic['videoInfo']['videos']['srcUrl']
#获取真确的视频连接
video = srcUrl.replace(systemTime,"cont-{}".format(video_id))  #获取到真确的视频链接
video_type = video.split('.')[-1]  #获取视频格式
# 下载视频
with open('videos/{}.{}'.format(video_id,video_type),mode='wb') as f:    #拼接视频文件名称并打开
    f.write(requests.get(video).content)   # 和图片保存方式一样

print("Over !!!!")