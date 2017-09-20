#! usr/bin/python
#coding=utf-8




def main():
    print("欢迎使用迷你待办事项管理程序")
    user_name = input("请输入用户名")
    user_password = input("请输入密码")
    #TODO(bb):用户名  密码验证
    print("请输入一个要进行的操作，如果不清楚，请输入H获取帮助")
    while(1):
        input_cmd = input()
        if(input_cmd == 'q'):
            break;
        elif(input_cmd=='r'):
            break;



main()