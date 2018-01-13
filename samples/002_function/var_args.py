#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')


# 作业:
def product(*nums):
    if len(nums) == 0:
        raise TypeError('Please input one number at least.')
    p = 1
    for n in nums:
        p *= n
    return p


from functools import reduce
def product(*nums):
    return reduce(lambda x, y: x*y, args)
