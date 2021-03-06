#! usr/bin/python
#coding=utf-8

'''
模块名称：
模块主要功能：
模块实现的方法：
模块对外接口：
模块作者：
编写时间：
修改说明：
修改时间：
'''

import todoFile

def todoQueryNewID(queryMode):
    if queryMode=='queryInTxt':
        return todoQueryNewIDInTxt()
    elif queryMode=='queryInSql':
        pass
    elif queryMode=='queryInExcel':
        pass
    else:
        pass


def todoQueryNewIDInTxt():
    curID = todoFile.todoFileOpt('readFile', 'getID')
    return curID+1

def todoQueryAllTodo():
    todoDicts = todoFile.todoFileOpt('fileRead', 'getTodoAll')
    for todoDict in todoDicts:
        print(str(todoDict))

def todoQueryTodoByID(todoID):
    todoDict = todoFile.todoFileOpt('fileRead', 'getTodobyID', todoID)