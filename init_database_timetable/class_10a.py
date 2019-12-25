from models import TimetableDay, TimetableClass, SchoolClass

if SchoolClass.get_class_by_name("10a") is None:
    school_class = SchoolClass("10a", "", 6)
    school_class.save()

if TimetableClass.get_by_id(10) is None:
    timetable_day = TimetableClass(46, 47, 48, 49, 50)
    timetable_day.save()

#177 - 196
if TimetableDay.get_by_id(46) is None:
    monday = TimetableDay(180, 181, None, None, None, 177, 178, 179)
    monday.save()

if TimetableDay.get_by_id(47) is None:
    tuesday = TimetableDay(185, 186, 187, None, None, 182, 183, 184)
    tuesday.save()

if TimetableDay.get_by_id(48) is None:
    wednesday = TimetableDay(191, 192, None, None, None, 188, 189, 190)
    wednesday.save()

if TimetableDay.get_by_id(49) is None:
    thursday = TimetableDay(196, 177, None, None, None, 193, 194, 195)
    thursday.save()

if TimetableDay.get_by_id(50) is None:
    friday = TimetableDay(181, 182, 183, None, None, 178, 179, 180)
    friday.save()
