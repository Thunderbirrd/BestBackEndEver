from models import TimetableDay, TimetableClass

#  аргумент это номер класса(id его будущий)
if TimetableClass.get_by_id(4) is None:
    timetable_class = TimetableClass(16, 17, 18, 19, 20)
    timetable_class.save()

if TimetableDay.get_by_id(16) is None:
    monday = TimetableDay(None, None, 1, 5, 9, 16, None, None)
    monday.save()

if TimetableDay.get_by_id(17) is None:
    tuesday = TimetableDay(None, None, 5, 6, 9, 17, None, None)
    tuesday.save()

if TimetableDay.get_by_id(18) is None:
    wednesday = TimetableDay(None, None, 15, 16, 17, 6, None, None)
    wednesday.save()

if TimetableDay.get_by_id(19) is None:
    thursday = TimetableDay(None, None, 5, 6, 9, 17, None, None)
    thursday.save()

if TimetableDay.get_by_id(20) is None:
    friday = TimetableDay(None, None, 1, 5, 9, 16, None, None)
    friday.save()
