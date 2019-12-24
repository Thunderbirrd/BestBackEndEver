from models import TimetableDay, TimetableClass

if TimetableClass.get_by_id(6) is None:
    timetable_Day = TimetableClass(26, 27, 28, 29, 30)
    timetable_day.save()
if TimetableDay.get_by_id(26) is None:
    monday = TimetableDay(6, 7, 9, 10, 3, 18, None, None)
    monday.save()
if TimetableDay.get_by_id(27) is None:
    tuesday = TimetableDay(19, 20, 5, 2, 1, 4, None, None)
    tuesday.save()
if TimetableDay.get_by_id(28) is None:
    wednesday = TimetableDay(8, 4, 9, 12, 7, None, None, None)
    wednesday.save()
if TimetableDay.get_by_id(29) is None:
    thursday = TimetableDay(1, 2, 10, 4, 8, None, None, None)
    thursday.save()
if TimetableDay.get_by_id(30) is None:
    friday = TimetableDay(7, 3, 4, 9, 10, 13, None, None)
    friday.save()