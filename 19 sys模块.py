# -*- coding:utf-8 -*-
# author: xiaoming


import sys

# path变量
# print(sys.path)

# 命令行参数，第一个为文件本身
# print(sys.argv)

# 拷贝文件
# src_file = sys.argv[1]
# dst_file = sys.argv[2]
#
# with open(r'%s' %src_file, mode='rt', encoding='utf-8') as f_read,\
#     open(r'%s' %dst_file, mode='wt', encoding='utf-8') as f_write:
#     for line in f_read:
#         f_write.write(line)

# 打印进度条
import time

recv_size = 0
total_size = 1025

def progress(percent):
    if percent > 1:
        percent = 1
    res = int(50 * percent) * '#'
    print('\r[%-50s] %d%%' %(res,int(100*percent)),end='')

while recv_size < total_size:
    time.sleep(0.02)
    recv_size += 1024
    percent = recv_size / total_size
    progress(percent)