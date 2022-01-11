#协程：为了保证CPU一直处理想要处理的程序，而不是去处理和程序无关的其他事务。
import asyncio
import time
async def func1():    #函数前加 async 切换为异步函数
    print("hello 11")
    await asyncio.sleep(3)    #异步操作的代码在此处。 比如：requests.get()    await:表示后台挂起，释放CPU
    print("hello 11")

async def func2():
    print("hello 22")
    await asyncio.sleep(2)
    print("hello 22")

async def func3():
    print("hello 33")
    await asyncio.sleep(4)
    print("hello 33")

async def main():
    # tasks = [func1(),func2(),func3()]  #func1() 此时的函数是异步协程函数，函数执行得到的是一个协程对象
    # await asyncio.wait(tasks)    #
    # #在python 3.8 以后的版本 使用以上方式会报错，推荐直接使用以下方式，代码如下
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks)   #必须使用await 挂起任务，否则报错

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())   #协程程序运行需要 asyncio模块支持， 此处为执行任务列表的固定搭配
    t2 = time.time()
    print(t2 - t1)        #如果串行了至少需要9秒， 通过协程处理后只需要4秒多。