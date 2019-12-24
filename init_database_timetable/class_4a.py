from models import TimetableDay, TimetableClass

#  аргумент это номер класса(id его будущий)
if TimetableClass.get_by_id(4) is None:
    timetable_class = TimetableClass(16, 17, 18, 19, 20)
    timetable_class.save()

if TimetableDay.get_by_id(16) is None:
    monday = TimetableDay(None, None, 42, 43, 44, 45, None, None)
    monday.save()

if TimetableDay.get_by_id(17) is None:
    tuesday = TimetableDay(None, None, 46, 47, 48, 42, None, None)
    tuesday.save()

if TimetableDay.get_by_id(18) is None:
    wednesday = TimetableDay(None, None, 46, 45, 44, 43, None, None)
    wednesday.save()

if TimetableDay.get_by_id(19) is None:
    thursday = TimetableDay(None, None, 43, 42, 48, 47, None, None)
    thursday.save()

if TimetableDay.get_by_id(20) is None:
    friday = TimetableDay(None, None, 47, 46, 45, 44, None, None)
    friday.save()
