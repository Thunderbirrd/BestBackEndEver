from models import TimetableDay, TimetableClass, SchoolClass

if SchoolClass.get_class_by_name("7a") is None:
    school_class = SchoolClass("7a", "", 3)
    school_class.save()

if TimetableClass.get_by_id(7) is None:
    timetable_day = TimetableClass(31, 32, 33, 34, 35)
    timetable_day.save()

#117 - 136
if TimetableDay.get_by_id(31) is None:
    monday = TimetableDay(None, None, 117, 118, 119, 120, 121, None)
    monday.save()
if TimetableDay.get_by_id(32) is None:
    tuesday = TimetableDay(None, None, 122, 123, 124, 125, 126, 127)
    tuesday.save()
if TimetableDay.get_by_id(33) is None:
    wednesday = TimetableDay(None, None, 128, 129, 130, 131, 132, None)#Начиная с этого не менял
    wednesday.save()
if TimetableDay.get_by_id(34) is None:
    thursday = TimetableDay(None, None, 133, 134, 135, 136, 117, None)
    thursday.save()
if TimetableDay.get_by_id(35) is None:
    friday = TimetableDay(None, None, 118, 119, 120, 121, 122, 123)
    friday.save()
