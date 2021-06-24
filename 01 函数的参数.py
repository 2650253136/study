# -*- coding:utf-8 -*-
# author: xiaoming

'''
1.位置参数
2.默认参数
3.可变参数
4.关键字参数
5.命名关键字参数
'''


# 1.位置参数,必须按照位置传参
def calc1(x,y):
    print(x,y)

# 2.默认参数,必须要在位置参数的后面
def calc2(x,y,z=3):
    print(x,y,z)

# 3.可变参数,可变长度的位置参数,*,用来接收溢出的位置实参,会被*处理,保存成元组的格式
def calc3(x,y,*args):
    print(x,y,args)
# calc3(1,2,3,4,5)

# 4.关键字参数,可变长度的关键字参数,**,用来接收溢出的关键字实参,会被**处理,保存成字典的格式
def calc4(x,y,*args,**kwargs):
    print(x,y,args,kwargs)
# calc4(1,2,3,4,5,a=6,b=7,c=8,d=9)

# 5.命名关键字参数,*后面定义的形参
def calc5(x,y,*,a,b):
    print(x,y,a,b)

# 6.组合使用
# 位置>默认>可变>命名关键字>关键字
def calc6(a,b,h=1,*args,c,d,**kwargs):
    print(a,b,h,args,c,d,kwargs)
# calc6(1,2,3,4,5,c=1,d=2,e=3,f=6,g=9)

# 7.函数传参的两种方式
# 7.1：
import requests
def get(url):
    response=requests.get(url)
    print(response.text)
# get('https://www.baidu.com')

# 7.2
def outter(url):
    def get():
        response=requests.get(url)
        print(response.text)
    return get
f=outter('https://www.baidu.com')
# f()