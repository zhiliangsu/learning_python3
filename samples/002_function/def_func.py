#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi/6)
print(x, y)

#TypeError: bad operand type:
my_abs('123')


def quadratic(a, b, c):
    if not (isinstance(a,(int, float)) and isinstance(b,(int, float)) and isinstance(c,(int, float))):
        raise TypeError('bad operand type')    
    elif a == 0:
        return('此方程不是一元二次方程')

    delta = b**2 - 4*a*c
    if delta < 0:
        return('此一元二次方程无实数根')
    elif delta == 0:
        return('此一元二次方程的根为：x1=x2=%f' % (-b/2*a))
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return x1, x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))