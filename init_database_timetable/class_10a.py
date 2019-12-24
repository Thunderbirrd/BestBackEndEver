from models import TimetableDay, TimetableClass

if TimetableClass.get_by_id(10) is None:
    timetable_day = TimetableClass(46, 47, 48, 49, 50)
    timetable_day.save()

if TimetableDay.get_by_id(46) is None:
    monday = TimetableDay(8, 9, 5, 12, 3, 3, 7, None)
    monday.save()

if TimetableDay.get_by_id(47) is None:
    tuesday = TimetableDay(7, 7, 20, 18, 4, 5, 5, None)
    tuesday.save()

if TimetableDay.get_by_id(48) is None:
    wednesday = TimetableDay(9, 9, 13, 3, 5, 9, None, None)
    wednesday.save()

if TimetableDay.get_by_id(49) is None:
    thursday = TimetableDay(8, 8, 12, 12, 14, 14, None, None)
    thursday.save()

if TimetableDay.get_by_id(50) is None:
    friday = TimetableDay(19, 2, 2, 1, 1, 9, 9, None)
    friday.save()
