from models import TimetableDay, TimetableClass, SchoolClass

if SchoolClass.get_class_by_name("6a") is None:
    school_class = SchoolClass("6a", "", 2)
    school_class.save()

if TimetableClass.get_by_id(6) is None:
    timetable_day = TimetableClass(26, 27, 28, 29, 30)
    timetable_day.save()
#97 - 116
if TimetableDay.get_by_id(26) is None:
    monday = TimetableDay(None, 97, 98, 99, 100, 101, None, None)
    monday.save()
if TimetableDay.get_by_id(27) is None:
    tuesday = TimetableDay(None, 102, 103, 104, 105, 106, 107, None)
    tuesday.save()
if TimetableDay.get_by_id(28) is None:
    wednesday = TimetableDay(None, 108, 109, 110, 111, 112, None, None)
    wednesday.save()
if TimetableDay.get_by_id(29) is None:
    thursday = TimetableDay(None, 113, 114, 115, 116, 97, None, None)
    thursday.save()
if TimetableDay.get_by_id(30) is None:
    friday = TimetableDay(None, 98, 99, 100, 101, 102, 103, None)
    friday.save()
