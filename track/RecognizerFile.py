# -*- coding: cp936 -*-

import sys
import os
from ctypes import *


class Recgonizier():
	def __init__(self):
		# print('>>>正在初始化...')

		self.YDMApi = windll.LoadLibrary('yundamaAPI')

		self.appId = 4960
		self.appKey = b'041208ab081235ba18d3b0998336157d'

		# print('软件ＩＤ：%d\r\n软件密钥：%s' % (self.appId, self.appKey))

		self.username = b'dancer_normal'
		self.password = b'123457'

		# 第一步：初始化云打码，只需调用一次即可
		self.YDMApi.YDM_SetAppInfo(self.appId, self.appKey)
		# 第二步：登陆云打码账号，只需调用一次即可
		self.uid = self.YDMApi.YDM_Login(self.username, self.password)

		if self.username == b'test':
			exit('\r\n>>>请先设置用户名密码')


####################### 一键识别函数 YDM_EasyDecodeByPath #######################

	def esay_recognition(self, file_path):
		# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
		codetype = 1004

		# 分配30个字节存放识别结果
		result = c_char_p(b"                              ")

		# 识别超时时间 单位：秒
		timeout = 60

		# 验证码文件路径
		file_path = file_path.encode('utf-8')
		filename = file_path

		# 一键识别函数，无需调用 YDM_SetAppInfo 和 YDM_Login，适合脚本调用
		captchaId = self.YDMApi.YDM_EasyDecodeByPath(self.username, self.password, self.appId, self.appKey, filename, codetype, timeout, result)

		# print("一键识别：验证码ID：%d，识别结果：%s" % (captchaId, result.value))
		return result.value


########################## 普通识别函数 YDM_DecodeByPath #########################
	def normal_recognition(self, file_path):
		print('\r\n>>>正在登陆...')
		if uid > 0:
			balance = self.YDMApi.YDM_GetBalance(self.username, self.password)
			print('\r\n>>>正在普通识别...')
			codetype = 1004
			result = c_char_p(b"                              ")

			file_path = file_path.encode('utf-8')
			filename = file_path

			# 普通识别函数，需先调用 YDM_SetAppInfo 和 YDM_Login 初始化
			captchaId = YDMApi.YDM_DecodeByPath(filename, codetype, result)

		return result.value