import os
import time
from random import randint
from multiprocessing import Process


# 进程一:写代码
def coding(i):
    while True:
        print('开始写代码{0} runing ... PID:{1}'.format(i, os.getpid()))
        time.sleep(randint(1,3))
        print('写累了,休息一会儿,玩会微信')


# 进程二:玩微信
def play_weixin():
    while True:
        print('开始玩微信... PID{0}'.format(os.getpid()))
        time.sleep(randint(1,2))
        print('结束微信, 我要写代码...')


if __name__ == '__main__':
    p1 = Process(target=coding,args=(1,))
    p2 = Process(target=coding,args=(2,))
    p3 = Process(target=play_weixin)
    # 启动进程
    p1.start()
    # 阻塞进程p1
    p1.join()
    p2.start()
    p3.start()
    while True:
        time.sleep(3)
        print('我是祝进程,我的pid是{pid}'.format(pid=os.getpid()))
