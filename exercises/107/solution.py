# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:12:53 2015

@author: Ars
"""


def select_student(my_class, mark):
    accepted = []
    refused = []
    for student in my_class:
        if student[1] >= mark:
            accepted.append(student)
        elif student[1] < mark:
            refused.append(student)

    accepted = sorted(accepted, key=lambda score: score[1], reverse=True)
    refused = sorted(refused, key=lambda score: score[1])
    return {"Accepted": accepted,
            "Refused": refused}
