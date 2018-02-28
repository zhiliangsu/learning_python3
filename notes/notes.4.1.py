#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Notes: 4.1 高阶函数 (Higher-order function)
# 
# 1.函数本身也可以赋值给变量，即：变量可以指向函数
# 2.函数名其实就是指向函数的变量，对于abs()这个函数，完全可以
#   把函数名abs看出变量，它指向一个可以计算绝对值的函数！
# 3.变量可以指向函数，函数的参数能接收变量，那么一个函数就可以
#   接收另一个函数作为参数，这种函数就称之为高阶函数。
#   
# 一个最简单的高阶函数：
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

max, min = min, max
print(max(1,2,3,4,5))
print(min(1,2,3,4,5))


# 4.1.1 map()函数
# 
# map()函数接收两个参数，一个是函数，一个是Iterable
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# 
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
list(r)

# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，
# Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并
# 返回一个list。

# 把这个list的所有数字转为字符串
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 4.1.2 reduce()函数
# 
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须
# 接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其
# 效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 
# 比方说对一个序列求和，就可以用reduce实现：
from functools import reduce
def add(x, y):
    return x + y

reduce(add, [1, 3, 5, 7, 9])

# 当然求和运算可以直接用Python內建函数sum()，没必要动用reduce。
# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def fn(x, y):
    return x * 10 + y

reduce(fn, [1, 3, 5, 7, 9])

# 这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，对上
# 的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
def char2num(s):
    digits = {
        '0': 0, '1': 1, '2': 2,
        '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9
    }
    return digits[s]

reduce(fn, map(char2num, '13579'))

# 整理成一个str2int的函数就是：
from functools import reduce

DIGITS = {
    '0': 0, '1': 1, '2': 2,
    '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9
}

# v1
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

# v2
def str2int(s):
    def char2num(s):
        return DIGITS[s]
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# 也就是说，假设Python没有提供int()函数，你完全可以自己写一个把
# 字符串转化成整数的函数，而且只需要几行代码!

# 练习1：
# 利用map()函数，把用户输入的不规范的英文名字，变成首字母大写，
# 其他小写的规范名字。
def normalize(name):
    return name.capitalize()
    # return name[0].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 练习2：
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()
# 函数，可以接受一个list并利用reduce求积。
from functools import reduce
def prod(L):
    return reduce(lambda x, y: x * y, L)
    # def plus(x, y):
    #     return x * y
    # return reduce(plus, L)

# 练习3：
# 利用map和reduce编写一个str2float函数，把字符串'123.456'
# 转换成浮点数123.456。
from functools import reduce

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

    