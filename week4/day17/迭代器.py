# __author__: wang_chongsheng
# date: 2017/9/25 0025

# list,tunple,dicy,string:Iterable（可迭代对象）

l = [1, 2, 3, 5]
d = iter(l)  # l.__iter__()
print(d)  # <list_iterator object at 0x0000017AFA524CC0>

# 什么是迭代器？
# 满足两个条件：1.有iter方法 2.有next方法

print(next(d))
#
# for 循环内部的三件事：
#     1.调用可迭代对象的iter方法返回一个迭代器对象
#     2.不断调用迭代器对象的next方法
#     3.处理StopIteration

for i in [1,2,34]:
    iter([1,2,34])
