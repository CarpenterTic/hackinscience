# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:12:53 2015

@author: Ars
"""
import string
alphabet1 = list(string.ascii_lowercase)
alphabet2 = list(string.ascii_lowercase)
for caract1 in (alphabet1):
    alphabet2.pop(0)
    for caract2 in alphabet2:
        print(caract1 + caract2)
