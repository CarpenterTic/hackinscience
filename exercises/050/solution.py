# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:12:53 2015

@author: Ars
"""
resultat = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        resultat += i
print(resultat)
