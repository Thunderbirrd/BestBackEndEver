from models import TimetableDay, TimetableClass, SchoolClass

if SchoolClass.get_class_by_name("9a") is None:
    school_class = SchoolClass("9a", "", 5)
    school_class.save()

if TimetableClass.get_by_id(9) is None:
    timetable_day = TimetableClass(41, 42, 43, 44, 45)
    timetable_day.save()

#157 - 176
if TimetableDay.get_by_id(41) is None:
    monday = TimetableDay(161, None, None, None, 157, 158, 159, 160)
    monday.save()

if TimetableDay.get_by_id(42) is None:
    tuesday = TimetableDay(166, 167, None, None, 162, 163, 164, 165)
    tuesday.save()

if TimetableDay.get_by_id(43) is None:
    wednesday = TimetableDay(172, None, None, None, 168, 169, 170, 171)
    wednesday.save()

if TimetableDay.get_by_id(44) is None:
    thursday = TimetableDay(157, None, None, None, 173, 174, 175, 176)
    thursday.save()

if TimetableDay.get_by_id(45) is None:
    friday = TimetableDay(162, 163, None, None, 158, 159, 160, 161)
    friday.save()
