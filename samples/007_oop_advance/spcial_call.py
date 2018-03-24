#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s' % self.name)

s = Student('Michael')
s()


# homework
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
    __call__ = __getattr__

print(Chain().status.user.timeline.list)
print(Chain().user('suzhiliang').repos)

# 1.关于__getattr__:
# 找不到 attr 就会调用 __getattr__ ，__getattr__ 继续返回 Chain 的实例，但是又没找到，于是在调用 __getattr__, 如此反复。
# print(Chain().status.user.timeline.list) 相当于Chain().__getattr__('status').__getattr__('user').__getattr__('timeline').__getattr__('list')
# 2.关于__call__:
# 一个可以将类实例变成一个可调用对象的方法,我们令__call__ = __getattr__,结合上一条，即将我们的Chain().users对象变成一个函数，
# 这个函数有两个参数，一个是self，还有一个是path，self是默认传入了的，所以我们只需要传入path