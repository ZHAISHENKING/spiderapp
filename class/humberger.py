import asyncio
import random


class Hamburger:

    @classmethod
    def make(cls, num, *args, **kwargs):
        hamburgers = []
        for i in range(num):
            hamburgers.append(cls.__new__(cls, *args, **kwargs))
        return hamburgers


# 创建5个Hamburger的实例
all_hamburger = Hamburger.make(5)


async def make_hamburger(num):
    """
    KFC根据顾客的请求做汉堡

    """
    # 使用count统计做的汉堡个数
    count = 0
    while True:
        if len(all_hamburger) == 0:
            await ask_for_hamburger()

        # 取出一个hanbuger
        hamburger = all_hamburger.pop()
        # 生成一个hamburger
        yield hamburger
        count += 1
        if count == num:
            break


async def ask_for_hamburger():
    """
    顾客请求汉堡
    """
    await asyncio.sleep(random.random())
    all_hamburger.extend(Hamburger.make(random.randint(1,10)))


async def buy_hamburgers():
    """
    购买汉堡
    """
    bucket = []
    async for p in make_hamburger(50):
        bucket.append(p)
        print('获得汉堡{}'.format(id(p)))


# 获得事件循环
loop = asyncio.get_event_loop()
res = loop.run_until_complete(buy_hamburgers())
loop.close()
