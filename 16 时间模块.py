# -*- coding:utf-8 -*-
# author: xiaoming

# 1.time
import time
# 时间分为三种格式
# 1.1 时间戳：从1970年到现在经过的秒数，用于时间间隔计算
print(time.time())
# 1.2 按照某种格式显示的时间：2021-06-22 11:48:36，用于展示时间
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y-%m-%d %X'))
# 1.3 结构化的时间，用于单独获取时间的一部分
res=time.localtime()
print(res.tm_year)

# 2.datetime
import datetime
print(datetime.datetime.now())
# 当前时间点往后推3天
print(datetime.datetime.now() + (datetime.timedelta(days=3)))

# 3.时间格式的转换
# 3.1 结构化时间与时间戳互相转换
# 结构化时间转时间戳
s_time=time.localtime()
print(time.mktime(s_time))
# 时间戳转换为结构化时间
tp_time=time.time()
print(time.localtime(tp_time))
# 3.2 结构化时间与格式化字符串时间互相转换
# 结构化时间转格式化字符串时间
s_time=time.localtime()
print(time.strftime('%Y-%m-%d %H:%M:%S',s_time))
# 格式化字符串时间转结构化时间
tp_time=time.strftime('%Y-%m-%d %H:%M:%S')
print(time.strptime(tp_time,'%Y-%m-%d %H:%M:%S'))
