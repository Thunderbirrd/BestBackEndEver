from models import TimetableDay, TimetableClass

#  аргумент это номер класса(id его будущий)
if TimetableClass.get_by_id(2) is None:
    timetable_class = TimetableClass(6, 7, 8, 9, 10)
    timetable_class.save()

if TimetableDay.get_by_id(6) is None:
    monday = TimetableDay(28, 29, 30, 31, None, None, None, None)
    monday.save()

if TimetableDay.get_by_id(7) is None:
    tuesday = TimetableDay(28, 34, 33, 32, None, None, None, None)
    tuesday.save()

if TimetableDay.get_by_id(8) is None:
    wednesday = TimetableDay(32, 31, 30, 29, None, None, None, None)
    wednesday.save()

if TimetableDay.get_by_id(9) is None:
    thursday = TimetableDay(29, 28, 34, 33, None, None, None, None)
    thursday.save()

if TimetableDay.get_by_id(10) is None:
    friday = TimetableDay(33, 32, 31, 30, None, None, None, None)
    friday.save()
