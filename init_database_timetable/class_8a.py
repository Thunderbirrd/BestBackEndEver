from models import TimetableDay, TimetableClass, SchoolClass

if SchoolClass.get_class_by_name("8a") is None:
    school_class = SchoolClass("8a", "", 4)
    school_class.save()

if TimetableClass.get_by_id(8) is None:
    timetable_day = TimetableClass(36, 37, 38, 39, 40)
    timetable_day.save()

#137 - 156
if TimetableDay.get_by_id(36) is None:
    monday = TimetableDay(None, None, None, 137, 138, 139, 140, 141)
    monday.save()
if TimetableDay.get_by_id(37) is None:
    tuesday = TimetableDay(147, None, None, 142, 143, 144, 145, 146)
    tuesday.save()
if TimetableDay.get_by_id(38) is None:
    wednesday = TimetableDay(None, None, None, 148, 149, 150, 151, 152)#Начиная с этого не менял
    wednesday.save()
if TimetableDay.get_by_id(39) is None:
    thursday = TimetableDay(None, None, None, 153, 154, 155, 156, 137)
    thursday.save()
if TimetableDay.get_by_id(40) is None:
    friday = TimetableDay(143, None, None, 138, 139, 140, 141, 142)
    friday.save()
