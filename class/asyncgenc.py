import types


def f():
    r = []
    for i in range(10):
        r.append(i)
    return r


def gen_f():
    for i in range(10):
        yield i


print(type(f()))
print(type(gen_f()))


import asyncio


async def async_f():
    r = []
    for i in range(10):
        r.append(i)
    return r

print(type(async_f()))


# 异步生成器函数
async def async_gen_f():
    await aaa()


async def aaa():
    pass


print(type(f) is types.FunctionType)
print(type(gen_f()) is types.GeneratorType)
print(type(async_f()) is types.CoroutineType)
