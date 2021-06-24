# -*- coding:utf-8 -*-
# author: xiaoming


# 1.大前提
# 闭包函数=名称空间与作用域+函数嵌套+函数对象
# 核心点：名字的查找关系是以函数定义阶段为准

# 2.什么是闭包函数
# "闭"函数指的该函数是内嵌函数
# "包"函数指的该函数包含对外层函数作用域名字的引用

# 闭包函数：函数对象
def f1():
    x=3333
    def f2():
        print(x)
    return f2
res=f1()
res()

# 3.闭包函数的应用