# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:12:53 2015

@author: Ars
"""


def sort_a_list(l):
    x = sorted(l, reverse=True)
    return x


# hg = range(0, 10)
# print((sort_a_list(hg)))


def sort_by_mark(my_class):
    x = sorted(my_class, reverse=True)
    return x


# classe1 = [[6, 'Joshua Tran'], [37, 'Jeanette Wafer'], [85, 'Susan Maddox'],
#            [84, 'Joseph Pedersen'], [12, 'Bonnie Torres'],
#            [36, 'John Freeman'], [27, 'Betty Askins'], [22, 'Mark Osbourne'],
#            [42, 'Lidia Robel']]
# print((sort_by_mark(classe1)))


def sort_by_name(my_class):
    y = sorted(my_class, key=lambda student: student[1])
    return y

# print(sort_by_name(classe1))
