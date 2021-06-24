# -*- coding:utf-8 -*-
# author: xiaoming


# 1.什么是哈希hash
# hash是一类算法，该算法接收传入的内容，经过运算得到一串hash值
# hash值特点：
    # 1.1 只要传入的内容一样，得到的hash值就一样
    # 1.2 不能由hash值反解成内容
    # 1.3 只要使用的hash算法不变，无论校验的内容有多大，得到的hash值长度是固定的

# 2.hash的用途
# 123456abc ==> hash字符串
        # 特点1.2 用于密码密文传输校验
        # 特点1.1、1.3 用于文件完整性校验

# 3.如何用
# import hashlib
# m = hashlib.md5()
# m.update('abc123@#%'.encode('utf-8'))
# res = m.hexdigest()
# print(res)

# 4.模拟撞库破解
# import hashlib
#
# cryptograph='284f3d09ea0695538e4ded1c1766d73a'
# # 密码字典
# passwds=[
#     'xiaoming12',
#     'xiaoming888',
#     '123xiaoming',
#     'xiaoming@123',
#     'xiaoming123'
# ]
# dic = {}
# for n in passwds:
#     res = hashlib.md5(n.encode('utf-8'))
#     dic[n] = res.hexdigest()
# # print(dic)
# # 模拟撞库得到明文密码
# for k,v in dic.items():
#     if v == cryptograph:
#         print('撞库成功，明文密码是: %s' %k)
#         break

# 5.密码加盐
# 提升撞库的成本
# import hashlib
# m=hashlib.md5()
# m.update('天王'.encode('utf-8'))
# m.update('alex3714'.encode('utf-8'))
# m.update('盖地虎'.encode('utf-8'))
# print(m.hexdigest())
