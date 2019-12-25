from models import TimetableDay, TimetableClass, SchoolClass

if SchoolClass.get_class_by_name("3a") is None:
    school_class = SchoolClass("3a", "", 23)
    school_class.save()

#  аргумент это номер класса(id его будущий)
if TimetableClass.get_by_id(3) is None:
    timetable_class = TimetableClass(11, 12, 13, 14, 15)
    timetable_class.save()

#83 - 89

if TimetableDay.get_by_id(11) is None:
    monday = TimetableDay(None, None, 83, 84, 85, 86, None, None)
    monday.save()

if TimetableDay.get_by_id(12) is None:
    tuesday = TimetableDay(None, None, 87, 88, 89, 83, None, None)
    tuesday.save()

if TimetableDay.get_by_id(13) is None:
    wednesday = TimetableDay(None, None, 84, 85, 86, 87, None, None)
    wednesday.save()

if TimetableDay.get_by_id(14) is None:
    thursday = TimetableDay(None, None, 88, 89, 83, 84, None, None)
    thursday.save()

if TimetableDay.get_by_id(15) is None:
    friday = TimetableDay(None, None, 85, 86, 87, 88, None, None)
    friday.save()
