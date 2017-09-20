# __author__: wang_chongsheng
# date: 2017/9/20 0020

# 集合的创建

# a=[1,2,3]
# b=list([4,5,6])
# print(a)
# print(b)

# s = ['Alice','Lucy','Luci']
# s1 = set(s)
# print(s1,type (s1))
# li = [1, 2, 'a']
# s = set(li)
# print(s)
# #
# print(2 in s)
# s.add('u')
# print(s)
# s.add('uu') #添加一个元素
# print(s)

# s.update('o000s')#做一个序列，将序列内容添加到数据里面
# print(s)
# s.update([1,'qwe'])
# print(s)

# s.remove(2)
# print(s)

# s.pop()
# print(s)

# s.clear()
# print(s)
# del s
# print(s)

# 集合操作符：in  in not
# print(set('Alice') == set('Alilice'))   #等价
# print(set('Alice') < set('Alicexxx'))   #子集
#
# print(set('Alice') and set('Alicexxx')) #取并集
# print(set('Alice') or set('Alicexxx')) #取交集

a = set([1, 2, 3, 4, 5])
b = set([4,5,6,7,8])

#intersection() 交集
print(a.intersection(b))