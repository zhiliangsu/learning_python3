#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])


# homework
# v1
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

# v2
def trim(s):
    if s == '':
        return s
    while s[0] == ' ' and len(s)>1:
        s = s[1:]
    while s[-1] == ' ' and len(s)>1:
        s = [:-1]
    return s