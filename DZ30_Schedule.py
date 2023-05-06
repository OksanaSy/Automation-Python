"""
Занятия проходят по понедельникам и четвергам в 19:15
Первое занятие произошло 27.03.2023.
Вывести список всех занятий в таком формате (номера лекций выровнены по правому краю):

Lecture  1: 27 Mar 2023 19:15
Lecture  2: 30 Mar 2023 19:15
Lecture  3: 03 Apr 2023 19:15
...
Lecture  9: 24 Apr 2023 19:15
Lecture 10: 27 Apr 2023 19:15
...
Lecture 32: 13 Jul 2023 19:15
"""

import datetime

currentMon = datetime.datetime(2023, 3, 27, 19, 15)
currentTue = currentMon + datetime.timedelta(days=3)
lecture = 1
while lecture <= 32:
    print("Lecture {:>2}: {:>2}".format(lecture, currentMon.strftime('%d %b %Y %H:%M')))
    currentMon = currentMon + datetime.timedelta(weeks=1)
    lecture += 1
    print("Lecture {:>2}: {:>2}".format(lecture, currentTue.strftime('%d %b %Y %H:%M')))
    currentTue = currentTue + datetime.timedelta(weeks=1)
    lecture += 1
