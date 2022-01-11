from threading import Thread    #线程类
from concurrent.futures import ThreadPoolExecutor      #线程池
# 多线程方式
def fn(name):
    for i in range(10):
        print('线程{}'.format(name),i)

if __name__ == '__main__':
    t = Thread(target=fn,args=("jj",))    # target 指定任务名称， args:传入参数，必须为数组类型，后边的逗号不能缺
    t.start()    #指定多线程状态为可执行状态，具体执行时间又CPU决定
    for i in range(20):
        print('main',i)

#多线程方式二
class myThread(Thread):
    def run(self):
        for i in range(10):
            print('子线程',i)

if __name__ == '__main__':
    t = myThread()
    t.start()     #千万不要t.run()  --》方法调用，单线程
    for i in range(10):
        print('main',i)

# 线程池
def fn1(name):    #创建一个需要执行的任务，name:可传入参数
    for i in range(10):
        print(name,i)

if __name__ == '__main__':
    with ThreadPoolExecutor(3) as t:    #创建一个有3个线程的线程池
        for i in range(20):     #有20个任务
            t.submit(fn1, name = '线程{}'.format(i))  #将任务逐个提交到线程池

    print("Over !!!")   #等待线程池执行完成之后，才继续执行（守护）