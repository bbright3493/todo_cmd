#! usr/bin/python
#coding=utf-8

import todoQuery
import todoRec

def main():
    print("欢迎使用迷你待办事项管理程序")
    #user_name = input("请输入用户名")
    #user_password = input("请输入密码")
    #TODO(bb):用户名  密码验证
    #登录后列出该用户所有待办事项
    print('您当前的待办事项如下：')
    todoQuery.todoQueryAllTodo()
    while(1):
        print("请输入一个要进行的操作，如果不清楚，请输入H获取帮助")
        input_cmd = input()
        if(input_cmd == 'q'):
            print('退出智能笔记本')
            break;
        elif(input_cmd=='r'):
            todoRec.todoRecMain()
        elif(input_cmd=='c'):
            todoRec.todoRecChangeLog()



main()