#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    
    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        if 0 <= score <= 100:
            self._score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

print('DO NOT use bart._Student__name:', bart._Student__name)



# homework 1
# 请把下面的Student对象的gender字段对外隐藏起来，
# 并用get_gender()和set_gender()代替，并检查参数有效性：

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('Not a valid parameter')
