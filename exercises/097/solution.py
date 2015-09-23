# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:12:53 2015

@author: Ars
"""


def love_meet(alice, bob):
    alice = set(alice)
    bob = set(bob)
    return(alice.intersection(bob))


def affair_meet(bob, alice, silvester):
    alice = set(alice)
    bob = set(bob)
    silvester = set(silvester)
    ill = (alice.intersection(silvester))
    return(ill.difference(bob))
