from models import TimetableDay, TimetableClass, SchoolClass

if SchoolClass.get_class_by_name("1a") is None:
    school_class = SchoolClass("1a", "", 21)
    school_class.save()

#  аргумент это номер класса(id его будущий)
if TimetableClass.get_by_id(1) is None:
    timetable_class = TimetableClass(1, 2, 3, 4, 5)
    timetable_class.save()

if TimetableDay.get_by_id(1) is None:
    monday = TimetableDay(21, 22, 23, 24, None, None, None, None)
    monday.save()

if TimetableDay.get_by_id(2) is None:
    tuesday = TimetableDay(21, 27, 26, 25, None, None, None, None)
    tuesday.save()

if TimetableDay.get_by_id(3) is None:
    wednesday = TimetableDay(22, 23, 24, 25, None, None, None, None)
    wednesday.save()

if TimetableDay.get_by_id(4) is None:
    thursday = TimetableDay(26, 27, 21, 22, None, None, None, None)
    thursday.save()

if TimetableDay.get_by_id(5) is None:
    friday = TimetableDay(23, 24, 25, 26, None, None, None, None)
    friday.save()
