# -*- coding:utf-8 -*-
# author: xiaoming

"""
文件、文件夹、压缩包处理模块
"""

import shutil

# 将文件内容拷贝到另一个文件中
# 目标文件无需存在
# shutil.copyfileobj(open('old.xml','r'),open('new.xml','w'))

# 拷贝文件
# 目标文件无需存在
# shutil.copyfile('old.txt','new.txt')

# 仅拷贝权限,内容、组、用户均不变
# 目标文件必须存在
# shutil.copymode('old.txt','new.txt')

# 仅拷贝状态信息,mode bits,atime,mtime,flags
# shutil.copystat('old.txt','new.txt')

# 拷贝文件和权限
# shutil.copy('old.txt','new.txt')

# 递归删除文件夹下的内容
# shutil.rmtree('folder')

# 移动文件夹,重命名
# shutil.move('oldname','newname')

# 将/data下的数据打成压缩包
# shutil.make_archive('data_bak', 'gztar', root_dir='/data')

# 解压包
# import tarfile
# t = tarfile.open('/tmp/data_bak','r')
# t.extractall('/data')
# t.close()

