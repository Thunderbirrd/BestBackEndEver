from models import TimetableDay, TimetableClass, SchoolClass

if SchoolClass.get_class_by_name("3a") is None:
    school_class = SchoolClass("3a", "", 23)
    school_class.save()

#  аргумент это номер класса(id его будущий)
if TimetableClass.get_by_id(3) is None:
    timetable_class = TimetableClass(11, 12, 13, 14, 15)
    timetable_class.save()

if TimetableDay.get_by_id(11) is None:
    monday = TimetableDay(None, None, 35, 36, 37, 38, None, None)
    monday.save()

if TimetableDay.get_by_id(12) is None:
    tuesday = TimetableDay(None, None, 39, 40, 41, 35, None, None)
    tuesday.save()

if TimetableDay.get_by_id(13) is None:
    wednesday = TimetableDay(None, None, 36, 37, 38, 39, None, None)
    wednesday.save()

if TimetableDay.get_by_id(14) is None:
    thursday = TimetableDay(None, None, 40, 41, 35, 36, None, None)
    thursday.save()

if TimetableDay.get_by_id(15) is None:
    friday = TimetableDay(None, None, 37, 38, 39, 40, None, None)
    friday.save()
