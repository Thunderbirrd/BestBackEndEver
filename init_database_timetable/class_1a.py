from models import TimetableDay, TimetableClass

#аргумент это номер класса(id его будущий)
if TimetableClass.get_by_id(1) is None:
    timetable_class = TimetableClass(1, 2, 3, 4, 5)
    timetable_class.save()

if TimetableDay.get_by_id(1) is None:
    monday = TimetableDay(13, 5, 9, 1, None, None, None, None)
    monday.save()

if TimetableDay.get_by_id(2) is None:
    tuesday = TimetableDay(17, 5, 1, 15, None, None, None, None)
    tuesday.save()

if TimetableDay.get_by_id(3) is None:
    wednesday = TimetableDay(1, 16, 5, 5, None, None, None, None)
    wednesday.save()

if TimetableDay.get_by_id(4) is None:
    thursday = TimetableDay(4, 16, 17, 1, None, None, None, None)
    thursday.save()

if TimetableDay.get_by_id(5) is None:
    friday = TimetableDay(1, 4, 9, 15, None, None, None, None)
    friday.save()
