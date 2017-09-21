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
import os


BaseDir = os.getcwd()

def todoFileOpt(fileOpt, optCmd, *saveArgs):
    if fileOpt=='fileRead':
        if optCmd=='getIDList':
            todoStr = todoReadFile()
            return todoFileQueryIDList(todoStr)
        elif optCmd=='getTodobyID':
            todoStr = todoReadFile()
            return todoFileQueryByID(todoStr, saveArgs[2])
    elif fileOpt=='fileWrite':
        todoFileSave(saveArgs[0], saveArgs[1])


def todoFileQueryByID(todoStr, todoID):
    return todoStrConvertDict(todoStr)[todoID]


def todoReadFile():
    fileName = BaseDir + r'\todoSave.txt'
    with open(fileName, 'r+') as todoFile:
        if todoFile==None:
            print('open file fail')
            return None
        else:
            return todoFile.read()

def todoFileSave(todoStr, todoTime):
    fileName = BaseDir + r'\todoSave.txt'
    todoDict = {}
    #读取文件，得到id列表
    todoListID = todoFileQueryIDList(str(todoReadFile()))
    if todoListID!=[]:
        todoDict['ID'] = todoListID[-1] + 1
    else:
        todoDict['ID'] = 1
    todoDict['待办事项'] = todoStr
    todoDict['事项时间'] = todoTime
    todoStr = str(todoDict)+';'
    print(todoStr)
    with open(fileName, 'a+') as todoFile:
        if todoFile==None:
            print('open file fail')
            return None
        else:
            return todoFile.write(todoStr)


def todoStrConvertDict(todoStr):
    todoDicts = []
    if todoStr=='':
        return todoDicts
    todoStrSub = todoStr[:-1]#去掉最后一个‘；’号，便于转换成字典
    todoLists = todoStrSub.split(';')#转换成待办事项列表
    for todoList in todoLists:
        todoDict = eval(todoList)
        todoDicts.append(todoDict)
    return todoDicts

def todoFileQueryIDList(todoStr):
    todoIDList = []
    todoDicts = todoStrConvertDict(todoStr)

    if todoDicts==[]:
        return todoIDList

    for todoDict in todoDicts:
        todoIDList.append(todoDict['ID'])
    return todoIDList


def todoTestStr():
    return todoFileQueryIDList(str(todoReadFile()))#


todoFileSave(u'今天要吃饭', u'2017-09-21-09-21')

print (todoTestStr())