# -*- coding:utf-8 -*-
# author: xiaoming

import configparser


config=configparser.ConfigParser()
config.read('conf.ini')

# 获取所有sections
print(config.sections())

# 获取某一个sections下的所有options
print(config.options('sections1'))

# 获取items
print(config.items('sections1'))

# 获取指定key对应的value
print(config.get('sections1','name'))
print(config.getint('sections1','age'))