# -*- coding:utf-8 -*-
# author: xiaoming

from functools import wraps

# 知识储备1
# # 由于语法糖的限制，outter函数只能有一个参数，并且该参数是用来接收被装饰对象的内存地址
# def outter(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
# @outter
# def index(x,y):
#     """首页功能"""
#     print(x,y)


# def auth(db_type):
#     def deco(func):
#         def wrapper(*args,**kwargs):
#             name = input('your name >>: ').strip()
#             pwd = input('your password >>: ').strip()
#             if db_type == 'file':
#                 print('基于文件验证')
#                 if name == 'egon' and pwd == '123':
#                     print('login successful')
#                     res=func(*args,**kwargs)
#                     return res
#                 else:
#                     print('用户名密码错误')
#             elif db_type == 'mysql':
#                 print('基于数据库验证')
#             elif db_type == 'ldap':
#                 print('基于ldap验证')
#             else:
#                 print('不支持的验证类型')
#         return wrapper
#     return deco
#
# @auth(db_type='mysql')
# def index(x,y):
#     print('index-->%s:%s' %(x,y))
#
# index(1,2)

# 有参装饰器模板
# def auth(xx):
#     # xx = 111 ↑
#     def outter(func):
#         def wrapper(*args,**kwargs):
#             res=func(*args,**kwargs)
#             return res
#         return wrapper
#     return outter
#
# @auth(xx=111)   #有参装饰器(xx=111)
# def index(x,y):
#     pass