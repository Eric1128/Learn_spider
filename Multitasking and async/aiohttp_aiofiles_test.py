import requests
import aiohttp
import asyncio
from lxml import etree
import aiofiles   # 安装：pip install aiofiles


'''
    抓取西游记电子书
    url:http://www.kulemi.com/zt/7/   可以获取到 每一集的名称和 Url
    思路：
        同步操作访问主URL，获取每一回的URL和名称
        异步请求每一个子URL。下载内容
'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
}

async def download_txt(url,name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as resp:
            resp.encoding = 'UTF-8'
            html = etree.HTML(await resp.text())     #获取响应数据之前一定要使用 await 进行手动挂起
            resp.close()
            p_list = html.xpath('//div[@class = "chapter-content"]/p')
            # with open('book/{}.txt'.format(name),mode='w+',encoding='utf-8') as f:
            #     for p in p_list:
            #         f.writelines(p.xpath('./text()')[0]+ '\n')
            # 异步写入
            async with aiofiles.open('book/{}.txt'.format(name),mode='w+',encoding='utf-8') as f:   #异步写入
                for p in p_list:
                     await f.writelines(p.xpath('./text()')[0]+ '\n')
    print(name,'Over!!!!')

async def main(main_url):   #创建异步任务
    resp = requests.get(main_url,headers=headers)
    resp.encoding = 'UTF-8'
    html = etree.HTML(resp.text)
    resp.close()
    a_list = html.xpath('//ul[@class="catalog"][1]//a')
    tasks = []
    for a in a_list:
        name = a.xpath('./text()')[0]
        s_url = a.xpath('./@href')[0]
        tasks.append(asyncio.create_task(download_txt(s_url,name)))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    main_url = 'http://www.kulemi.com/zt/7/'
    asyncio.run(main(main_url))
