from multiprocessing import Process   #进程
from concurrent.futures import ProcessPoolExecutor   #进程池
#进程方法一
def fn(name):
    for i in range(10):
        print('子进程{}'.format(name),i)

if __name__ == '__main__':
    p = Process(target=fn,args=('jj',))
    p.start()
    p.join()
    for i in range(10):
        print('主进程',i)

#进程方法二
class myProcess(Process):
    def run(self):
        for i in range(10):
            print('子进程',i)

if __name__ == '__main__':
    p = myProcess()
    p.start()
    for i in range(10):
        print('主进程',i)

#进程池
def fn1(name,name1):
    for i in range(10):
        print('子进程{}'.format(name),i,name1)


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=10) as p:
        for i in range(20):
            p.submit(fn1,name=i,name1='b')  #传递参数
    print("Over !!!")   #等待进程池执行完成之后，才继续执行（守护）