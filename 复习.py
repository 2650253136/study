# -*- coding:utf-8 -*-
# author: xiaoming

# ---------------------------------1.函数的参数
# 位置参数
# def calc1(x,y):
#     print(x,y)
# calc1(1,2)
# 默认参数
# def calc2(x,y,z=3):
#     print(x,y,z)
# calc2(1,2)
# 可变参数-元组接收
# def calc3(x,y,*args):
#     print(x,y,args)
# calc3(1,2,3,4,5,6)
# 关键字参数-字典接收
# def calc4(x,y,*args,**kwargs):
#     print(x,y,args,kwargs)
# calc4(1,2,3,4,5,a=1,b=2,c=3)
# 函数传参的两种方式
# 一：
import requests
# def get(url):
#     response=requests.get(url)
#     print(response.text)
# get('https://www.baidu.com')
# 二：
# def outter(url):
#     def get():
#         response=requests.get(url)
#         print(response.text)
#     return get
# f=outter('https://www.baidu.com')
# f()
# ---------------------------------2.名称空间与作用域
# 名称空间：
    # 1.内置名称空间-python解释器内置的名字
        # python解释器启动则产生,关闭则销毁
    # 2.全局名称空间-只要不是函数内的,也不是内置的,剩下的都是全局名称
        # python文件执行则产生,运行完毕则销毁
    # 3.局部名称空间-调用函数时,运行函数体代码过程中产生的函数内的名字
        # 调用函数式产生,调用完毕后销毁
# 名称空间加载顺序：
    # 内置-->全局-->局部
# 名称空间销毁顺序：
    # 局部-->全局-->内置
# 名字的查找优先级
    # 当前局部-->局部>全局>内置
    # 当前全局-->全局>内置
# 作用域：作用范围
    # 全局作用域：内置名称空间、全局名称空间
    # 局部作用域：布局名称空间的名字
# global与nonlocal
    # global：如果在局部想要修改全局的名字对应的值(不可变类型), 需要用global声明
    # nonlocal：修改函数外层函数包含的名字对应的值(不可变类型), 需要用nonlocal声明
# ---------------------------------3.函数对象
# def func():
#     print('from func')
# 可以赋值
# f = func
# print(f,func)
# f()
# 可以当做函数参数传入
# def foo(x):
#     x()
# foo(func)
# 当做另外一个函数的返回值
# def foo1(x):
#     return x
# a = foo1(func)
# a()
# 当做一个容器类型的元素
# l = [func,]
# l[0]()
# k = {'k':func}
# k['k']()
# 案例：
# def login():
#     print('登录')
# def transfer():
#     print('转账')
# def check_banlance():
#     print('查询余额')
# func_dic = {
#     '0':('退出',None),
#     '1':('登录',login),
#     '2':('转账',transfer),
#     '3':('查询余额',check_banlance)
# }
# while True:
#     for k in func_dic:
#         print(k,func_dic[k][0])
#     choice = input('请输入命令编号：').strip()
#     if not choice.isdigit():
#         continue
#     if choice == '0':
#         break
#     if choice in func_dic:
#         func_dic[choice][1]()
#     else:
#         print('输入的指令不存在')
# ---------------------------------4.函数嵌套
# 嵌套定义：在函数内定义其它函数
# def foo1():
#     def foo2():
#         print('from foo2')
#     hello()
#     return foo2()
# foo1()
# 函数调用：在调用一个函数的过程中又调用其它函数
# def hello():
#     print('hello world')
# def foo1():
#     def foo2():
#         print('from foo2')
#     hello()
#     return foo2()
# foo1()
# ---------------------------------5.闭包函数
# 前提：
    # 闭包函数=名称空间与作用域+函数嵌套+函数对象
    # 核心点：名字的查找关系是以函数定义阶段为准
# 解释：
    # "闭"函数指该函数时内嵌函数
    # "包"函数指该函数包含对外层函数作用域名字的引用
# 闭包函数：函数对象
# def f1():
#     x=333
#     def f2():
#         print(x)
#     return f2
# res=f1()
# res()
# ---------------------------------6.装饰器
# 指定义一个函数,该函数是用来为其它函数添加额外的功能
# 开放封闭原则：
        # 开放：指的是对拓展功能是开放的
        # 封闭：指的是对修改源代码是封闭的
        # 在不修改被装饰器对象源代码以及调用方式的前提下为被装饰器对象添加新功能
# 案例一：添加代码运行时间统计
# import time
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         func(*args,**kwargs)
#         stop=time.time()
#         print('运行时长：%.f 秒' %(stop-start))
#     return wrapper
# @timmer
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s' %(x,y))
# index(11,22)
# 案例二：auth认证
# def auth(func):
#     def wrapper(*args,**kwargs):
#         name = input('username >>: ').strip()
#         pwd = input('password >>: ').strip()
#         if name == 'xiao' and pwd =='123':
#             res=func(*args,**kwargs)
#             return res
#         else:
#             print('用户名密码错误')
#     return wrapper
# @auth
# def index():
#     print('from index')
# index()

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
# ---------------------------------7.三元表达式
# 语法：x if x > y else y
# 条件成立时要返回的值 if 条件 else 条件不成立时要返回的值
# x = 31
# y = 222
# res=x if x > y else y
# print(res)
# ---------------------------------8.列表生成式
# 列表
# l = [n for n in range(10)]
# print(l)
# 字典
# k = {key:None for key in range(10)}
# print(k)
# ---------------------------------9.函数递归调用
# def f1():
#     print('is me...')
#     f1()
# f1()
# def f1(n):
#     if n == 20:
#         return
#     print(n)
#     n+=1
#     f1(n)
# f1(10)
# 递归调用案例：
# l = [1,2,[3,[4,[5,[6,[7,[8,[9,10,11]]]]]]]]
# def f1(list1):
#     for n in list1:
#         if type(n) is list:
#             f1(n)
#         else:
#             print(n)
# f1(l)
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------