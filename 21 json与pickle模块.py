# -*- coding:utf-8 -*-
# author: xiaoming

# 1.什么是序列化
# 指把内存的数据类型转换成一个特定的格式的内容
# 改格式的内容可用于存储或者传输给其它平台使用
# 序列化：内存中的数据类型——>序列化——>特定的格式(json、pickle)
# 反序列化：内存中的数据类型<——序列化<——特定的格式(json、pickle)


# 2.为何要序列化
# 可用于存储
# 可传输给其它平台


# 3.如何序列化与反序列化
import json
# # 序列化
# res = [1,'aaa',True,False]
# with open('test.json', mode='wt', encoding='utf-8') as f:
#     json.dump(res, f)
# # 反序列化
# with open('test.json', mode='rt', encoding='utf-8') as f:
#     res = json.load(f)
#     print(res)
# res = json.dumps([1,'aaa',True,False])
# print(res,type(res))
# res = json.loads('[1,"aaa",true,false]')
# print(res,type(res))


# 4.pickle模块, bytes
# import pickle
# # 序列化
# res=pickle.dumps({1,2,3,4,5})
# print(res,type(res))
# # 反序列化
# res1 = pickle.loads(res)
# print(res1,type(res1))