#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Notes: 2.3 函数的参数
# 
# 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。
# 对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。
# 
# Python的函数定义非常简单，但灵活度却非常大。
# 除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。


# 2.3.1 位置参数
# 
# 调用函数时，传入的值按照位置顺序依次赋给参数

# v1
def power(x):
    return x*x

power(5)
power(15)

# v2
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

power(5, 2)
power(5, 3)


# 2.3.2 默认参数
# v3
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

power(5)
power(5, 2)

# 从上面的例子可以看出，默认参数可以简化函数的调用。
# 设置默认参数时，有几点要注意：
#     1.必选参数在前，默认参数在后，否则Python的解释器会报错;
#     2.当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 使用默认参数最大的好处是可以降低调用函数的难度。

# eg1.enroll()函数需要传入两个参数
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

enroll('Sarah','F')

# 如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。
# eg2.在enroll()函数中把年龄和城市设为默认参数
#     这样大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数
#     只有与默认参数不符的学生才需要提供额外的信息
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Sarah','F')
enroll('Bob','M', 7)
enroll('Adam','M', city='Tianjin')

# 可见，默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以
# 传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个。
#     3.有多个默认参数时，调用的时候，既可以按顺序提供默认参数;
#       比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。
#     4.也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上;
#       比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。
#     5.默认参数必需指向不变对象！

# 为什么要设计str、None这样的不变对象呢？
# 因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误；
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。
# 我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。


# 2.3.3 可变参数
# 
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

calc([1, 2, 3])
calc((1, 3, 5, 7))


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1, 2, 3)
calc(1, 3, 5, 7)
calc(1, 2)
calc()
nums = [1, 2, 3]
calc(nums[0], nums[1], nums[2])
calc(*nums)


# 2.3.4 关键字参数
# 
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple；
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)


# 2.3.5 命名关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 如果要限制关键字参数的名字，就可以使用命名关键字参数，例如，
# 只接受city和job作为关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)

# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*, *后面
# 的参数被视为命名关键字参数。调用方式如下：
person('jack', 24, city='Beijing', job='Engineer')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数
# 就不再需要一个特殊分隔符*了。
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

# 命名关键字参数可以有缺省值，从而简化调用:
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

# 由于命名关键字参数city具有默认值，调用时，可不传入city参数:
person('Jack', 24, job='Engineer')

# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个
# *作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名
# 关键字参数:
def person(name, age, city, job):
    # 缺少*，city和job被视为位置参数
    pass


# 2.3.5 参数组合
#
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字
# 参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、
# 命名关键字参数和关键字参数。eg:
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

# 最神奇的是通过一个tuple和dict，你也可以调用上述函数:
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式
# 来调用它，无论它的参数是如何定义的。

# 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数
# 接口的可理解性很差。


# 2.3.6 小结
# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
# 要注意定义可变参数和关键字参数的语法：
#     *args是可变参数，args接收的是一个tuple；
#     **kw是关键字参数，kw接收的是一个dict。
# 以及调用函数时如何传入可变参数和关键字参数的语法：
#     可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#     关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
