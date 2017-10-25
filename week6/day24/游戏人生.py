# @Time    : 2017/10/25 23:24
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : 游戏人生.py
class PrintData:
    def show(self):
        print('姓名：%s,性别：%s,年龄：%s,你当前战斗力为：%s' % (self.name, self.gender, self.age, self.fight))
class Person(PrintData):
    def __init__(self,n,a,g,f):
        self.name = n
        self.age = a
        self.gender = g
        self.fight = f
    def  GrassBattle(self):
        self.fight = int(self.fight) - 200
        super(Person,self).show()
    def SelfCultivation(self):
        self.fight = self.fight + 100
        super(Person, self).show()
    def MultiplayerGames(self):
        self.fight = int(self.fight) - 500
        super(Person, self).show()
obj = Person('仓井井','女',18,2000)
# obj.GrassBattle()
# obj.SelfCultivation()
# obj.MultiplayerGames()

name = input('请输入名称：')
sex  = input('请输入性别：')
age  = int(input('请输入年龄：'))
fight= int(input('请输入战斗力：'))
obj = Person('%s'%(name),'%s'%(sex),'%s'%(age),'%s'%(fight))
print('------战斗类型-----')
print('-----1.草丛战斗----')
print('-----2.自我修炼----')
print('-----3.多人游戏----')
print('------q.退出-------')
enter = input('请输入战斗类型：')
if enter == 1:
    obj.GrassBattle()
# elif enter == 2:1
#     obj.SelfCultivation()
# elif enter == 3:
#     obj.MultiplayerGames()
# else:
#     print('Game over!')
#     exit()

