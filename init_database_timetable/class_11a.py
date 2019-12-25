from models import TimetableDay, TimetableClass, SchoolClass

if SchoolClass.get_class_by_name("11a") is None:
    school_class = SchoolClass("11a", "", 7)
    school_class.save()

if TimetableClass.get_by_id(11) is None:
    timetable_day = TimetableClass(51, 52, 53, 54, 55)
    timetable_day.save()

#197 - 216
if TimetableDay.get_by_id(51) is None:
    monday = TimetableDay(199, 200, 201, None, None, None, 197, 198)
    monday.save()

if TimetableDay.get_by_id(52) is None:
    monday = TimetableDay(204, 205, 206, 207, None, None, 202, 203)
    monday.save()

if TimetableDay.get_by_id(53) is None:
    monday = TimetableDay(210, 211, 212, None, None, None, 208, 209)
    monday.save()

if TimetableDay.get_by_id(54) is None:
    monday = TimetableDay(215, 216, 197, None, None, None, 213, 214)
    monday.save()

if TimetableDay.get_by_id(55) is None:
    monday = TimetableDay(200, 201, 202, 203, None, None, 198, 199)
    monday.save()
