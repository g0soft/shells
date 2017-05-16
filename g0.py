#!/usr/bin/env python3
import sys
from datetime import datetime


def titles(d):
    return '첫눈이 에피소드 No.' + str(getDays(d)) + ' -  제목 (' + d.strftime("%Y.%m.%d") + ')'


def getDays(d):
    return (d - datetime(2014, 8, 12)).days + 1


input = input("Input Date : ")

if len(input) == 6:
    print(titles(datetime.strptime(input, "%y%m%d")))
elif len(input) == 8:
    print(titles(datetime.strptime(input, "%Y%m%d")))
elif len(input) == 10:
    print(titles(datetime.strptime(input, "%Y.%m.%d")))
else:
    print(titles(datetime.today()))

