from models import TimetableDay, TimetableClass

if TimetableClass.get_by_id(9) is None:
    timetable_day = TimetableClass(41, 42, 43, 44, 45)
    timetable_day.save()

if TimetableDay.get_by_id(41) is None:
    monday = TimetableDay(7, 8, 4, 11, 2, 2, 6, None)
    monday.save()

if TimetableDay.get_by_id(42) is None:
    tuesday = TimetableDay(6, 6, 19, 17, 3, 4, 4, None)
    tuesday.save()

if TimetableDay.get_by_id(43) is None:
    wednesday = TimetableDay(8, 8, 12, 2, 4, 8, None, None)
    wednesday.save()

if TimetableDay.get_by_id(44) is None:
    thursday = TimetableDay(7, 7, 11, 11, 13, 13, None, None)
    thursday.save()

if TimetableDay.get_by_id(45) is None:
    friday = TimetableDay(18, 1, 1, 20, 2, 8, 8, None)
    friday.save()
