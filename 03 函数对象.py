# -*- coding:utf-8 -*-
# author: xiaoming


# func=内存地址
def func():
    print('from func')

# 1.可以赋值
# f=func
# print(f,func)
# f()

# 2.可以当做函数参数传入
# def foo(x):
#     x()
# foo(func)

# 3.当做另外一个函数的返回值
# def foo(x):
#     return x
# a = foo(func)
# a()

# 4.当做一个容器类型的元素
# l = [func,]
# l[0]()
# k = {'k1':func}
# k['k1']()


def login():
    print('登录')
def transfer():
    print('转账')
def check_banlance():
    print('查询余额')
def withdraw():
    print('提现')
def register():
    print('注册')

func_dic = {
    '0':('退出',None),
    '1':('登录',login),
    '2':('转账',transfer),
    '3':('查询余额',check_banlance),
    '4':('提现',withdraw),
    '5':('注册',register)
}

while True:
    for k in func_dic:
        print(k,func_dic[k][0])
    choice = input("请输入命令编号：").strip()
    if not choice.isdigit():
        continue
    if choice == '0':
        break
    if choice in func_dic:
        func_dic[choice][1]()
    else:
        print('输入的指令不存在')