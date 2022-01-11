#requests.get()同步的代码 --》 异步操作 aiohttp
import aiohttp  # 安装：pip install aiohttp
import asyncio

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
}

# 下载图片
img_urls = [
    "http://kr.shanghai-jiuxin.com/file/mm/20211130/yoqimyhyq5j.jpg",
    "http://kr.shanghai-jiuxin.com/file/mm/20211130/4bsggpt111d.jpg",
    "http://kr.shanghai-jiuxin.com/file/mm/20211130/kbjfm2p5yfg.jpg",
    ]

async def download_img(url):
    '''
        s = aiohttp.ClientSession()   等价于 requests
        s.get()   等价于  requests.get()
        s.post()   等价于  requests.post()
        headers 参数，添加请求头
        params 参数，GET请求参数
        data 参数，POST的body
        porxy 参数，代理相关
    '''
    '''
    img_name = url.rsplit('/',1)[-1]
    async with aiohttp.ClientSession() as session:  #固定搭配，加with 不用考虑session.close()
        async with session.get(url,headers=headers) as resp:    #发起请求
            #resp.text()     # 等于 requests 中的 resp.test  
            #resp.json()     # 等于 requests 中的 resp.json()
            #resp.content.read()  等于 requests 中的 resp.resp.content
            #获取如上响应数据之前一定要使用 await 进行手动挂起
            with open('img/{}'.format(img_name),mode='wb') as f:   #创建文件，  可以使用 aiofiles 模块异步操作
                f.write(await resp.content.read())      
    print(url,'搞定')
async def main():
    tasks=[]
    for url in img_urls:
        tasks.append(asyncio.create_task(download_img(url)))   #创建任务
    await asyncio.wait(tasks)        #启动并挂起任务

if __name__ == '__main__':
    asyncio.run(main())