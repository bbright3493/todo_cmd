#! usr/bin/python
#coding=utf-8

'''
模块名称：todoRec
模块主要功能：
该模块主要实现待办事项的录入
模块实现的方法：
todoRecMain
模块对外接口：
todoRecMain
模块作者：BB
编写时间：2017-09-20
修改说明：
修改时间：
'''



def todoRecMain():
	'''
	待办事项录入主控函数
	参数：
	返回值：
	'''
	print('请输入待办事项,按回车结束录入：')
	userTodoStr = input()
	#todo(bb):todoGetCurrentTime()
	#todo(bb):生成ID，规整化数据
	#todo(bb):todoSaveMain(...)
	print('您的待办事项"%s"已存储，当前ID是""', userTodoStr)
	
	


