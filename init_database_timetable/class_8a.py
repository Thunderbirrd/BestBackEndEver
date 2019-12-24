from models import TimetableDay, TimetableClass

if TimetableClass.get_by_id(8) is None:
    timetable_day = TimetableClass(36, 37, 38, 39, 40)
    timetable_day.save()

#137 - 156
if TimetableDay.get_by_id(36) is None:
    monday = TimetableDay(None, 137, 138, 139, 140, 141, 142, 143)
    monday.save()
if TimetableDay.get_by_id(37) is None:
    tuesday = TimetableDay(None, 144, 145, 146, 147, 148, 149, None)
    tuesday.save()
if TimetableDay.get_by_id(38) is None:
    wednesday = TimetableDay(None, 150, 151, 152, 153, 154, None, None)#Начиная с этого не менял
    wednesday.save()
if TimetableDay.get_by_id(39) is None:
    thursday = TimetableDay(None, 155, 156, 137, 138, 139, 140, None)
    thursday.save()
if TimetableDay.get_by_id(40) is None:
    friday = TimetableDay(None, 141, 142, 143, 144, 145, None, None)
    friday.save()
