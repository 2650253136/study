# # -*- coding:utf-8 -*-
# # author: xiaoming
#
#
# # 终端输出99乘法表
# # h = 1
# # while h <= 9:
# #     l = 1
# #     while l <= h:
# #         print('%s*%s=%s' %(l,h,h*l),end='\t')
# #         l += 1
# #     print('')
# #     h += 1
#
# # 1000以内的所有完数，例如6=1+2+3
#
#
# # 输入一个字符串，判断是否为回文：从左到右和从右到左读完全相同的字符串，例如abbc
# str_var='aabbaa'
# l_var = list(str_var)
# '''
# 0
# 1
# 2
# 3
# 4
# 5
# '''
# i = 0
# while i < len(l_var):
#     # print(i)
#
#     if l_var[i] == l_var[i]:
#         print('%s:%s' % (l_var[i], l_var[i]))
#     i+=1
#
#
# # 输入一行字符，分别统计英文字母、空格、数字和其它字符的个数
#
# # 计算两个大数相加的和，会超过int64的表示范围

# user_input = input('your input >>: ')
# list_var = [n for n in user_input]
# str1 = [n for n in list_var if n.isalpha()]
# num1 = [n for n in list_var if n.isdigit()]
# other1 = [n for n in list_var if not n.isdigit() and not n.isalpha() and not n.isspace()]
# space1 = [n for n in list_var if n.isspace()]
# for n in user_input:
#     list_var.append(n)
#     if n.isdigit():
#         num1.append(n)
#     elif n.isspace():
#         space1.append(n)
#     elif n.isalpha():
#         str1.append(n)
#     else:
#         other1.append(n)
# print('数字个数：%s' %(len(num1)))
# print('空格个数：%s' % (len(space1)))
# print('英文个数：%s' % (len(str1)))
# print('其它符号个数：%s' % (len(other1)))
