from models import TimetableDay, TimetableClass

if TimetableClass.get_by_id(7) is None:
    timetable_day = TimetableClass(31, 32, 33, 34, 35)
    timetable_day.save()

if TimetableDay.get_by_id(31) is None:
    monday = TimetableDay(3, 7, 1, 10, 9, 18, 14, None)
    monday.save()
if TimetableDay.get_by_id(32) is None:
    tuesday = TimetableDay(19, 8, 6, 2, 9, 4, None, None)
    tuesday.save()
if TimetableDay.get_by_id(33) is None:
    wednesday = TimetableDay(8, 4, 9, 12, 7, None, None, None)#Начиная с этого не менял
    wednesday.save()
if TimetableDay.get_by_id(34) is None:
    thursday = TimetableDay(1, 2, 10, 4, 8, None, None, None)
    thursday.save()
if TimetableDay.get_by_id(35) is None:
    friday = TimetableDay(7, 3, 4, 9, 10, 13, None, None)
    friday.save()