# -*- coding: cp936 -*-

import sys
import os
from ctypes import *


class Recgonizier():
	def __init__(self):
		# print('>>>���ڳ�ʼ��...')

		self.YDMApi = windll.LoadLibrary('yundamaAPI')

		self.appId = 4960
		self.appKey = b'041208ab081235ba18d3b0998336157d'

		# print('����ɣģ�%d\r\n�����Կ��%s' % (self.appId, self.appKey))

		self.username = b'dancer_normal'
		self.password = b'123457'

		# ��һ������ʼ���ƴ��룬ֻ�����һ�μ���
		self.YDMApi.YDM_SetAppInfo(self.appId, self.appKey)
		# �ڶ�������½�ƴ����˺ţ�ֻ�����һ�μ���
		self.uid = self.YDMApi.YDM_Login(self.username, self.password)

		if self.username == b'test':
			exit('\r\n>>>���������û�������')


####################### һ��ʶ���� YDM_EasyDecodeByPath #######################

	def esay_recognition(self, file_path):
		# ����1004��ʾ4λ��ĸ���֣���ͬ�����շѲ�ͬ����׼ȷ��д������Ӱ��ʶ���ʡ��ڴ˲�ѯ�������� http://www.yundama.com/price.html
		codetype = 1004

		# ����30���ֽڴ��ʶ����
		result = c_char_p(b"                              ")

		# ʶ��ʱʱ�� ��λ����
		timeout = 60

		# ��֤���ļ�·��
		file_path = file_path.encode('utf-8')
		filename = file_path

		# һ��ʶ������������� YDM_SetAppInfo �� YDM_Login���ʺϽű�����
		captchaId = self.YDMApi.YDM_EasyDecodeByPath(self.username, self.password, self.appId, self.appKey, filename, codetype, timeout, result)

		# print("һ��ʶ����֤��ID��%d��ʶ������%s" % (captchaId, result.value))
		return result.value


########################## ��ͨʶ���� YDM_DecodeByPath #########################
	def normal_recognition(self, file_path):
		print('\r\n>>>���ڵ�½...')
		if uid > 0:
			balance = self.YDMApi.YDM_GetBalance(self.username, self.password)
			print('\r\n>>>������ͨʶ��...')
			codetype = 1004
			result = c_char_p(b"                              ")

			file_path = file_path.encode('utf-8')
			filename = file_path

			# ��ͨʶ���������ȵ��� YDM_SetAppInfo �� YDM_Login ��ʼ��
			captchaId = YDMApi.YDM_DecodeByPath(filename, codetype, result)

		return result.value