from models import TimetableDay, TimetableClass

#аргумент это номер класса(id его будущий)
if TimetableClass.get_by_id(3) is None:
    timetable_class = TimetableClass(11, 12, 13, 14, 15)
    timetable_class.save()

if TimetableDay.get_by_id(11) is None:
    monday = TimetableDay(None, None, 5, 9, 6, 1, None, None)
    monday.save()

if TimetableDay.get_by_id(12) is None:
    tuesday = TimetableDay(None, None, 8, 9, 16, 17, None, None)
    tuesday.save()

if TimetableDay.get_by_id(13) is None:
    wednesday = TimetableDay(None, None, 15, 4, 12, 15, None, None)
    wednesday.save()

if TimetableDay.get_by_id(14) is None:
    thursday = TimetableDay(None, None, 1, 12, 5, 6, None, None)
    thursday.save()

if TimetableDay.get_by_id(15) is None:
    friday = TimetableDay(None, None, 16, 17, 9, 1, None, None)
    friday.save()
