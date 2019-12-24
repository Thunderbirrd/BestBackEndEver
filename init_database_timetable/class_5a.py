from models import TimetableDay, TimetableClass, SchoolClass

if SchoolClass.get_class_by_name("5a") is None:
    school_class = SchoolClass("5a", "", 1)
    school_class.save()

if TimetableClass.get_by_id(5) is None:
    timetable_day = TimetableClass(21, 22, 23, 24, 25)
    timetable_day.save()

if TimetableDay.get_by_id(21) is None:
    monday = TimetableDay(6, 7, 8, 9, 10, None, None, None)
    monday.save()

if TimetableDay.get_by_id(22) is None:
    tuesday = TimetableDay(11, 12, 13, 14, 15, 16, None, None)
    tuesday.save()

if TimetableDay.get_by_id(23) is None:
    wednesday = TimetableDay(17, 18, 19, 20, 1, None, None, None)
    wednesday.save()

if TimetableDay.get_by_id(24) is None:
    thursday = TimetableDay(2, 3, 4, 5, 6, None, None, None)
    thursday.save()

if TimetableDay.get_by_id(25) is None:
    friday = TimetableDay(7, 8, 9, 10, 11, 12, None, None)
    friday.save()
