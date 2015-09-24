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
            accepted.append(student)
        elif mark < student[1]:
            refused.append(student)

    sorted_desc = sorted(accepted, key=lambda score: score[1], reverse=True)
    sorted_asc = sorted(refused, key=lambda score: score[1])
    return {"Accepted": sorted_desc,
            "Refused": sorted_asc}
