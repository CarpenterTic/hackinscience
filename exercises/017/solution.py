# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:07:17 2015

@author: Ars
"""

import sys
if len(sys.argv) == 3:
    print(int(sys.argv[1]) + int(sys.argv[2]))
else:
    print("usage: python3 solution.py OP1 OP2")
