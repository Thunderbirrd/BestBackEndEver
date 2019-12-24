from models import TimetableDay, TimetableClass

if TimetableClass.get_by_id(5) is None:
    timetable_Day = TimetableClass(21, 22, 23, 24, 25)
    timetable_day.save()

if TimetableDay.get_by_id(21) is None:
    monday = TimetableDay(9, 3, 4, 7, 19, None, None, None)
    monday.save()

if TimetableDay.get_by_id(22) is None:
    tuesday = TimetableDay(6, 6, 4, 2, 10, 5, None, None)
    tuesday.save()

if TimetableDay.get_by_id(23) is None:
    wednesday = TimetableDay(18, 20, 9, 10, 8, None, None, None)
    wednesday.save()

if TimetableDay.get_by_id(24) is None:
    thursday = TimetableDay(14, 13, 12, 3, 4, None, None, None)
    thursday.save()

if TimetableDay.get_by_id(25) is None:
    friday = TimetableDay(9, 10, 1, 2, 8, 10, None, None)
    friday.save()