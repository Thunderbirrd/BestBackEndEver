from models import TimetableDay, TimetableClass

#  аргумент это номер класса(id его будущий)
if TimetableClass.get_by_id(2) is None:
    timetable_class = TimetableClass(6, 7, 8, 9, 10)
    timetable_class.save()

if TimetableDay.get_by_id(6) is None:
    monday = TimetableDay(5, 15, 6, 12, None, None, None, None)
    monday.save()

if TimetableDay.get_by_id(7) is None:
    tuesday = TimetableDay(17, 16, 5, 9, None, None, None, None)
    tuesday.save()

if TimetableDay.get_by_id(8) is None:
    wednesday = TimetableDay(8, 5, 15, 4, None, None, None, None)
    wednesday.save()

if TimetableDay.get_by_id(9) is None:
    thursday = TimetableDay(5, 16, 6, 12, None, None, None, None)
    thursday.save()

if TimetableDay.get_by_id(10) is None:
    friday = TimetableDay(1, 12, 5, 6, None, None, None, None)
    friday.save()
