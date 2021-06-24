# -*- coding:utf-8 -*-
# author: xiaoming


# 1.列表生成式
# l = ['alex_dsb','xiaob_dsb','mos_dsb','xiaoming']
# new_l = []
# for name in l:
#     if name.endswith('dsb'):
#         new_l.append(name)
# print(new_l)
#
# # 方案二：列表生成式
# new_l = [name for name in l if name.endswith('dsb')]
# print(new_l)

# 案例一：所有小写字母换成大写
# new_l = [name.upper() for name in l]
# print(new_l)

# 案例二：所有名字去掉后缀_dsb
# new_l = [name.replace('_dsb','') for name in l]
# print(new_l)

# 2.字典生成式
# keys=['name','age','gender']
# dic = {key:None for key in keys}
# print(dic)
# items=[('name','xiaom'),('age',18),('gender','male')]
# res={k:v for k,v in items}
# print(res,type(res))

# 3.集合生成式
# l=['name','age','gender']
# set1={key for key in l}
# print(set1,type(set1))

# 4.生成式表达式
# g = (i for i in range(18) if i > 3)
## 此时g内部没有值，next后才会产生值
# print(g,type(g))

# print(next(g))