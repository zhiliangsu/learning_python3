#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2018-2-28')

now()



def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('DEBUG')
def today():
    print('2018-2-28')

today()
print(today.__name__)


# homework 1
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        func = fn(*args, **kw)
        runtime = time.time() - start
        print('%s executed in %s ms' % (fn.__name__, runtime))
        return func
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


# homework 2
import functools
def log(text):
    if not isinstance(text, str):
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('begin call: calling %s()' % text.__name__)
            fn = text(*args, **kw)
            print('end call.')
            return fn
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin call: %s %s()' % (text, func.__name__))
                fn = func(*args, **kw)
                print('end call.')
            return wrapper
        return decorator

@log
def now():
    print('2018-2-28 hello')

@log('execute')
def now():
    print('2018-2-28 hello')