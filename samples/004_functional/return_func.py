#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print(f)
print(f())


# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


# fix
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


# homework
# v1
def createrCounter():
    n = 0
    def counter():
        nonlocal n
        n += 1
        return n
    return counter

# v2
def createrCounter():
    n = [0]
    def counter():
        nonlocal n
        n[0] += 1
        return n[0]
    return counter

# v3 generator
def createrCounter():
    def g():
        n = 0
        while True:
            n += 1
            yiedl n
    it = g()
    def counter():
        return next(it)
    return counter