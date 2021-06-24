# -*- coding:utf-8 -*-
# author: xiaoming


# 1.什么是装饰器
# 装饰器指的是定义一个函数，该函数是用来为其它函数添加额外的功能

# 2.为何要用装饰器
# 开放封闭原则
    # 开放：指的是对拓展功能是开放的
    # 封闭：指的是对修改源代码是封闭的
# 在不修改被装饰器对象源代码以及调用方式的前提下为被装饰对象添加新功能

# 3.如何用装饰器
import time
# def index(x,y):
#     start=time.time()
#     print('index %s %s' %(x,y))
#     time.sleep(3)
#     stop=time.time()
#     print(stop - start)
# index(111,222)

# def index(x,y):
#     time.sleep(3)
#     print('index %s %s' %(x,y))
# def outter(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         func(*args,**kwargs)
#         stop=time.time()
#         print(stop - start)
#     return wrapper
# index = outter(index)
# index(111,222)

# def home(name):
#     time.sleep(3)
#     print('welcome %s to page' %name)
#     return 12345
# def outter(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         res = func(*args,**kwargs)
#         stop = time.time()
#         print(stop-start)
#         return res
#     return wrapper
# home = outter(home)
# res=home('xiaoming')
# print(res)

# 4.语法糖
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         res = func(*args,**kwargs)
#         stop = time.time()
#         print('运行时长：%.f 秒' %(stop-start))
#         return res
#     return wrapper
# @timmer
# def home(name):
#     time.sleep(3)
#     print('welcome %s to page' %name)
# home('xiaoming')

# 5.总结无参装饰器的模板
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         # 1.调用原函数
#         # 2.为其增加新功能
#         start = time.time()
#         res=func(*args,**kwargs)
#         stop = time.time()
#         print(stop - start)
#         return res
#     return wrapper
# @timmer
# def index():
#     print('from index')
# index()

def auth(func):
    # 将原函数的属性赋值给wrapper
    from functools import wraps
    @wraps(func)
    def wrapper(*args,**kwargs):
        # 1.调用原函数
        # 2.为其增加新功能
        name = input('Enter your username >>:').strip()
        pwd = input('Enter your password >>:').strip()
        if name == 'xiao' and pwd == '123':
            res=func(*args,**kwargs)
            return res
        else:
            print('账户密码错误')
    return wrapper
#
@auth
def index():
    """注释111"""
    print('from index')
index()