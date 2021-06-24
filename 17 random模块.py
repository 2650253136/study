# -*- coding:utf-8 -*-
# author: xiaoming

import random

# 大于等于1且小于等于5之间的整数
# print(random.randint(1,5))

# 大于等于1且小于5之间的整数
# print(random.randrange(1,5))

# 从列表中随机取指定个数元素
# print(random.sample(['xiaoming','bingbing','xiaohu','moshang'],2))

# 取大于1且小于3直接的浮点数
# print(random.uniform(1,3))

# 应用：随机验证码
def make_code(size=6):
    res=''
    for i in range(size):
        num1=str(random.randint(0,9))
        str1=chr(random.randint(97,122))
        # 随机字符=random.choice([26个大写字母随机取出一个,10个数字中随机取出一个])
        res+=random.choice([num1,str1])
    return res
print(make_code(4))