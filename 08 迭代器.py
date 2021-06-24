# -*- coding:utf-8 -*-
# author: xiaoming


# 1.什么是迭代器
# 迭代器指的是迭代取值的工具，迭代是一个重复的过程，每次重复都是基于上一次的结果而继续的，单纯的重复并不是迭代

# 2.为何要有迭代器
# 涉及把多个值循环取出来的类型有：列表，字符串，元组，字典，集合，打开文件
# count = 0
# while count < 5:
#     print(count)
#     count += 1

# l = ['xi','ha','he']
# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1

# 3.如何用迭代器
# 可迭代对象：内置有__iter__方法的都称之为可迭代的对象

# 调用可迭代对象下面的__iter__方法会将其转换为迭代器对象
# d={'a':1,'b':2}
# res=d.__iter__()
# while True:
#     try:
#         print(res.__next__())
#     except StopIteration:
#         break

# for循环工作原理：迭代器循环
# d={'a':1,'b':2}
# 1.d.__iter__()得到一个迭代器对象
# 2.迭代器对象.__next__()拿到一个返回值，然后将该返回值赋值给k
# 3.循环步骤2，直到抛出StopIteration异常, for循环会捕捉异常然后结束循环
# for k in d:
#     print(k)

# 4.迭代器优缺点总结
# 不能控制索引取值
# 一次性，取完了就只能重新定义