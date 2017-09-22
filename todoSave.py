#! usr/bin/python
#coding=utf-8

'''
模块名称：todoSave
模块主要功能：保存待办事项和用户信息数据
模块实现的方法：
todoSaveTodo:保存待办事项
todoSaveUser:保存用户信息数据
模块对外接口：
todoSaveTodo
todoSaveUser
模块作者：
编写时间：
修改说明：
修改时间：
'''
import os

def todoSaveTodo(saveData, saveMode='saveToTxt'):
	'''
	函数名称：todoSaveTodo
	函数参数：
	saveData:需要存储的数据
	saveMode:存储模式 saveToTxt:存到文本文件里面 saveToCsv:存到CSV文件里面 saveToMysql：存到mysql数据库里面
	返回值：无
	'''
	if saveMode=='saveToTxt':
		todoSaveTodoTxt(saveData)
	elif saveMode=='saveToCsv':
		todoSaveTodoCsv(saveData)
	elif saveMode=='saveToMysql':
		todoSaveTodoMysql(saveData)
	else:
		pass
		
BaseDir = os.getcwd()
		
def todoSaveTodoTxt(saveData):
	fileName = BaseDir + r''
	#打开文件，写入文件
	with open(fileName, 'w') as todoFile:
		todoFile.write(saveData)
	
		
def todoSaveTodoCsv(saveData):
	pass

def todoSaveTodoMysql(saveData):
	pass


