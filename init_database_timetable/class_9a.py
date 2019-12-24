from models import TimetableDay, TimetableClass

if TimetableClass.get_by_id(9) is None:
    timetable_day = TimetableClass(41, 42, 43, 44, 45)
    timetable_day.save()

#157 - 176
if TimetableDay.get_by_id(41) is None:
    monday = TimetableDay(157, 158, 159, 160, 161, 162, 163, None)
    monday.save()

if TimetableDay.get_by_id(42) is None:
    tuesday = TimetableDay(164, 165, 166, 167, 168, 169, 170, None)
    tuesday.save()

if TimetableDay.get_by_id(43) is None:
    wednesday = TimetableDay(171, 172, 173, 174, 175, 176, None, None)
    wednesday.save()

if TimetableDay.get_by_id(44) is None:
    thursday = TimetableDay(157, 158, 159, 160, 161, 162, None, None)
    thursday.save()

if TimetableDay.get_by_id(45) is None:
    friday = TimetableDay(163, 164, 165, 166, 167, 168, 169, None)
    friday.save()
