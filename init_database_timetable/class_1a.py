from models import TimetableDay, TimetableClass, SchoolClass

if SchoolClass.get_class_by_name("1a") is None:
    school_class = SchoolClass("1a", "", 21)
    school_class.save()

#  аргумент это номер класса(id его будущий)
if TimetableClass.get_by_id(1) is None:
    timetable_class = TimetableClass(1, 2, 3, 4, 5)
    timetable_class.save()

#69 - 75

if TimetableDay.get_by_id(1) is None:
    monday = TimetableDay(69, 70, 71, 72, None, None, None, None)
    monday.save()

if TimetableDay.get_by_id(2) is None:
    tuesday = TimetableDay(73, 74, 75, 69, None, None, None, None)
    tuesday.save()

if TimetableDay.get_by_id(3) is None:
    wednesday = TimetableDay(70, 71, 72, 73, None, None, None, None)
    wednesday.save()

if TimetableDay.get_by_id(4) is None:
    thursday = TimetableDay(74, 75, 69, 70, None, None, None, None)
    thursday.save()

if TimetableDay.get_by_id(5) is None:
    friday = TimetableDay(71, 72, 73, 74, None, None, None, None)
    friday.save()
