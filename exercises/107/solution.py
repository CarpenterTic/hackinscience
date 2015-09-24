# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:12:53 2015

@author: Ars
"""


def select_student(my_class, mark):
    accepted = []
    refused = []
    for student in my_class:
        if mark >= student[1]:
            Accepted.append(student)
        if mark < student[1]:
            Refused.append(student)

    sorted_asc = sorted(accepted, key=lambda score: score[1])
    sorted_desc = sorted(refused, key=lambda score: score[1], reverse=True)
    return {"Accepted": sorted_desc,
            "Refused": sorted_asc}
