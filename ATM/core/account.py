# __author__: wang_chongsheng
# date: 2017/10/24 0024
import json
def acc_register():
    reg_id=input("请输入卡号: ")
    reg_pwd=input("请输入密码: ")
    again_pwd=input("请再次输入密码: ")
    if again_pwd != reg_pwd:
        print('你输入的密码不匹配！')
    reg_info = {reg_id:reg_pwd}
    data = json.dumps(reg_info)
    f = open('../db/1234.json','w')
    json.dump(reg_info,f)
    f.close()

# acc_register()

def