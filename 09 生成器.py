# -*- coding:utf-8 -*-
# author: xiaoming

# 在函数内一旦存在yield关键字，调用函数并不会执行函数体代码，会返回一个生成器对象，就是一个自定义迭代器
def func():
    yield 1
    yield 2
    yield 3
    yield 4

a=func()
# print(a)

# 生成器就是迭代器
# a.__iter__()
# a.__next__()
# 会触发函数体代码的第一次运行，然后遇到yield停下来，将yield后的值当做本次调用的结果返回
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# next(a)
# iter(a)