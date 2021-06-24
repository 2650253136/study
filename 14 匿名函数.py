# -*- coding:utf-8 -*-
# author: xiaoming

# 1.有名函数
def func(x,y):
    return x+y

# 2.lambda用于定义匿名函数
# print(lambda x,y:x+y)

# 3.调用匿名函数
# res=lambda x,y:x+y
# print(res(111,222))

# 4.匿名函数的应用
salary={
    'tom':7000,
    'xiaoming':10000,
    'hes':2000
}
# res=max(salary,key=lambda k:salary[k])
# print(res)
# res1=min(salary,key=lambda x:salary[x])
# print(res1)

# 5.sorted排序,reverse=True=从大到小排序
res=sorted(salary,key=lambda k:salary[k],reverse=True)
print(res)