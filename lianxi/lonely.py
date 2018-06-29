import time
from random import randint


def get_up():
    print('开始起床')
    time.sleep(randint(10,20))
    print('起床完毕...')


def go_to_class():
    print('我要上学校，花儿对我笑')
    time.sleep(randint(5,10))
    print('到班里了')


get_up()
go_to_class()