from models import TimetableDay, TimetableClass, SchoolClass

if SchoolClass.get_class_by_name("2a") is None:
    school_class = SchoolClass("2a", "", 22)
    school_class.save()

#  аргумент это номер класса(id его будущий)
if TimetableClass.get_by_id(2) is None:
    timetable_class = TimetableClass(6, 7, 8, 9, 10)
    timetable_class.save()

#76 - 82

if TimetableDay.get_by_id(6) is None:
    monday = TimetableDay(81, 82, 76, 77, None, None, None, None)
    monday.save()

if TimetableDay.get_by_id(7) is None:
    tuesday = TimetableDay(78, 79, 80, 81, None, None, None, None)
    tuesday.save()

if TimetableDay.get_by_id(8) is None:
    wednesday = TimetableDay(82, 76, 77, 78, None, None, None, None)
    wednesday.save()

if TimetableDay.get_by_id(9) is None:
    thursday = TimetableDay(79, 80, 81, 82, None, None, None, None)
    thursday.save()

if TimetableDay.get_by_id(10) is None:
    friday = TimetableDay(76, 77, 78, 79, None, None, None, None)
    friday.save()
