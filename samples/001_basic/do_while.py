#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 计算1+2+3+...+100:
sum = 0
n = 1
while n <= 100:
    sum += n
    n += 1
print(sum)

# 计算1x2x3x...x100:
acc = 100
n = 1
while n <= 100:
    acc *= n
    n += 1
print(acc)