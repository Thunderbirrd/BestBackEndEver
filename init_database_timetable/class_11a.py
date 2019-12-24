from models import TimetableDay, TimetableClass

if TimetableClass.get_by_id(11) is None:
    timetable_day = TimetableClass(51, 52, 53, 54, 55)
    timetable_day.save()

#197 - 216
if TimetableDay.get_by_id(51) is None:
    monday = TimetableDay(216, 215, 214, 213, 212, 211, None, None)
    monday.save()

if TimetableDay.get_by_id(52) is None:
    monday = TimetableDay(210, 209, 208, 207, 206, 205, 204, None)
    monday.save()

if TimetableDay.get_by_id(53) is None:
    monday = TimetableDay(203, 202, 201, 200, 199, 198, None, None)
    monday.save()

if TimetableDay.get_by_id(54) is None:
    monday = TimetableDay(197, 216, 215, 214, 213, 212, 211, None)
    monday.save()

if TimetableDay.get_by_id(55) is None:
    monday = TimetableDay(210, 209, 208, 207, 206, 205, None, None)
    monday.save()
