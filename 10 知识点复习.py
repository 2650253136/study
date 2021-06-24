# -*- coding:utf-8 -*-
# author: xiaoming


"""
1.有参装饰器auth
    from functools import wraps
    def auth(db_type)
        def outter(func):
            # 相同属性
            @wraps(func)
            def wrapper(*args,**kwargs):
                # 添加新功能
                res=func(*args,**kwargs)
                return res
            return wrapper
        return outter

2.分析@auth(db_type='file')的执行过程
    @auth(db_type='file') ==> @outter ==> 原函数名=outter(被装饰的函数)

3.简述什么是可迭代对象, 什么是迭代器对象
    可以转换成迭代器的对象__iter__为可迭代对象
    既有__iter__方法也有__next__方法的为迭代器对象

4.简述迭代器的优缺点
    一次性
    不能控制索引取值

5.简述for循环工作原理
    for k in 可迭代对象:
        print(k)
    # 1.__iter__()得到一个迭代器对象
    # 2.迭代器对象.__next__()拿到一个返回值，然后将该返回值赋值给k
    # 3.循环步骤2，直到抛出StopIteration异常, for循环会捕捉异常然后结束循环

6.自定义迭代器实现range功能

"""