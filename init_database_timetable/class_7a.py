from models import TimetableDay, TimetableClass

if TimetableClass.get_by_id(7) is None:
    timetable_day = TimetableClass(31, 32, 33, 34, 35)
    timetable_day.save()

#117 - 136
if TimetableDay.get_by_id(31) is None:
    monday = TimetableDay(117, 118, 119, 120, 121, 122, 123, None)
    monday.save()
if TimetableDay.get_by_id(32) is None:
    tuesday = TimetableDay(124, 125, 126, 127, 128, 129, None, None)
    tuesday.save()
if TimetableDay.get_by_id(33) is None:
    wednesday = TimetableDay(130, 131, 132, 133, 134, None, None, None)#Начиная с этого не менял
    wednesday.save()
if TimetableDay.get_by_id(34) is None:
    thursday = TimetableDay(135, 136, 117, 118, 119, 120, None, None)
    thursday.save()
if TimetableDay.get_by_id(35) is None:
    friday = TimetableDay(121, 122, 123, 124, 125, None, None, None)
    friday.save()
