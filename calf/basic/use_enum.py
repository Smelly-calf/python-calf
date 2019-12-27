#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


if __name__ == '__main__':
    print(Weekday.Sun)
    day1 = Weekday.Sun
    print(day1 == Weekday.Sun)  # True
    print(day1.value == Weekday.Sun)  # False
    print(day1.value == Weekday.Sun.value)  # True

    print(Weekday.Sun)
    print(Weekday.Sun.name)
    print(Weekday.Sun.value)

