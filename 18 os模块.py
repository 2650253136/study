# -*- coding:utf-8 -*-
# author: xiaoming

import os

# 查看文件夹下面的子文件以及子文件夹名
# print(os.listdir(r'C:\python\mode'))

# 递归创建空文件夹
# os.makedirs('dir1/dir2')

# 若目录为空，则删除
# os.removedirs('dir1')

# 创建单级目录
# os.mkdir('dir1')

# 删除单级空目录
# os.rmdir('dir1')

# 删除一个文件
# os.remove('file1')

# 重命名文件
# os.rename('oldfile','newfole')

# 获取文件大小
# print(os.path.getsize('filename'))

# 执行shell命令，直接输出结果
# os.system('df -h')

# 判断path是一个存在的文件
# os.path.isfile('file')

# 判断path是一个存在的目录
# os.path.isdir('dirname')

# path路径拼接
# print(os.path.join('aaa','bbb','ccc.txt'))

# 获取系统环境变量
# print(os.environ)

# 返回path规范化的绝对路径
# print(os.path.abspath('.'))
# print(os.path.dirname(__file__))

# 将path分割成目录和文件名
# print(os.path.split(r'C:\python\study\16 时间模块.py'))

