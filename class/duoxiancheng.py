# # /usr/bin/env python
# # 导入时间模块
# import time
# # 多线程模块
# import threading
#
#
# class Job(threading.Thread):
#
#     def __init__(self, dbname):
#         """
#         创建 Job的实例
#         :param dbname:
#         """
#         super(Job, self).__init__()
#         self.dbname = dbname
#
#     def run(self):
#         print("开始备份数据{0}".format(self.dbname))
#         if self.dbname == 'database1':
#             time.sleep(5)
#         time.sleep(5)
#         print("数据库{0}".format(self.dbname))
#
#
# # 使用多线程备份
# # 一个线程就是一个实例
# task1 = Job('database1')
# task2 = Job('database2')
#
# task1.start()
# task2.start()
#
# task1.daemon = True
# task2.daemon = True
#
# # 线程阻塞
# task1.join()
# task2.join()
#
#
# print('备份完成')

import threading
import time


class A(threading.Thread):

    def __init__(self, dbname):
        super(A, self).__init__()
        self.dbname = dbname

    def run(self):
        print(self.dbname)
        time.sleep(5)
        print("{}备份完成".format(self.dbname))


task1 = A('db1')
task2 = A('db2')

task1.start()
task2.start()

task1.join()
task2.join()

print("备份完成")