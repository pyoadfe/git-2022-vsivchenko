# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 13:53:51 2022

@author: cosbo
"""


students = []

with open("students.txt") as f:
    for line in f:
        students.append(line)
students.sort()
a = list(set(students))

res = []
for i in students:
    if i not in res:
        res.append(i)

with open('students.txt', 'w') as w:
    for r in res:
        w.write(r)