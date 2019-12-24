from models import TimetableDay, TimetableClass, SchoolClass

if SchoolClass.get_class_by_name("10a") is None:
    school_class = SchoolClass("10a", "", 6)
    school_class.save()

if TimetableClass.get_by_id(10) is None:
    timetable_day = TimetableClass(46, 47, 48, 49, 50)
    timetable_day.save()

#177 - 196
if TimetableDay.get_by_id(46) is None:
    monday = TimetableDay(177, 178, 179, 180, 181, 182, 183, None)
    monday.save()

if TimetableDay.get_by_id(47) is None:
    tuesday = TimetableDay(184, 185, 186, 187, 188, 189, 190, None)
    tuesday.save()

if TimetableDay.get_by_id(48) is None:
    wednesday = TimetableDay(191, 192, 193, 194, 195, 196, None, None)
    wednesday.save()

if TimetableDay.get_by_id(49) is None:
    thursday = TimetableDay(177, 178, 179, 180, 181, 182, None, None)
    thursday.save()

if TimetableDay.get_by_id(50) is None:
    friday = TimetableDay(183, 184, 185, 186, 187, 188, 189, None)
    friday.save()
