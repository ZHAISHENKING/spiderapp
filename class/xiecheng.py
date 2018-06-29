import time


def buy():
    """
    买汉堡
    """
    result = ''
    while True:
        n = yield result
        if not n:
            return
        print('顾客{0}'.format(n))
        time.sleep(2)
        result = 'Done'


def make(c):
    """
    做汉堡
    """
    next(c)
    n = 0
    while n<5:
        n = n+1
        print('做汉堡{0}'.format(n))
        r = c.send(n)
        print('买汉堡{0}'.format(r))
    c.close()


if __name__ == '__main__':
    c = buy()
    make(c)