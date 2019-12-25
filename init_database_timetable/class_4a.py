from models import TimetableDay, TimetableClass, SchoolClass

if SchoolClass.get_class_by_name("4a") is None:
    school_class = SchoolClass("4a", "", 24)
    school_class.save()

#  аргумент это номер класса(id его будущий)
if TimetableClass.get_by_id(4) is None:
    timetable_class = TimetableClass(16, 17, 18, 19, 20)
    timetable_class.save()
    
#90 - 96

if TimetableDay.get_by_id(16) is None:
    monday = TimetableDay(None, None, 90, 91, 92, 93, None, None)
    monday.save()

if TimetableDay.get_by_id(17) is None:
    tuesday = TimetableDay(None, None, 94, 95, 96, 90, None, None)
    tuesday.save()

if TimetableDay.get_by_id(18) is None:
    wednesday = TimetableDay(None, None, 91, 92, 93, 94, None, None)
    wednesday.save()

if TimetableDay.get_by_id(19) is None:
    thursday = TimetableDay(None, None, 95, 96, 90, 91, None, None)
    thursday.save()

if TimetableDay.get_by_id(20) is None:
    friday = TimetableDay(None, None, 92, 93, 94, 95, None, None)
    friday.save()
