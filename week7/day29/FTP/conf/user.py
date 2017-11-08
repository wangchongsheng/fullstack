# @Time    : 2017/11/8 0008 11:20
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : user.py

import os,socket,time,pickle

class User:
    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd
        print(self.name,self.passwd)
    def Register(self):
        pickle.dump((open('../db/user_info'),'wb'),self.name)
        # f = open('../db/user_info','a')
        # f.write(self.name,self.passwd)
        # f.close()

    def Login(self):
        pass
    def Logout(self):
        pass

reg_usr = str(input("Enter Username: "))
reg_pwd = str(input("Enter Password: "))
r = User(reg_usr,reg_pwd)
r.Register()