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

import time
import todoFile

def todoRecMain():
    print("请输入待办事项")
    userTodoStr = input()
    userTodoTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    userTodoLog = '待办'
    todoFile.todoFileOpt('fileWrite', 'writeOneRec', userTodoStr, userTodoTime, userTodoLog)
    print('您的待办事项%s已存储'%(userTodoStr))
	
	
def todoRecChangeLog():
    print('请输入要改变状态的ID号')
    userTodoID = input()



