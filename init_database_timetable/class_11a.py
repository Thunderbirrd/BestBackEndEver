from models import TimetableDay

if TimetableDay.get_by_id(51) is None:
    monday = TimetableDay(10, 10, 3, 3, 6, 6, None, None)
    monday.save()

if TimetableDay.get_by_id(52) is None:
    monday = TimetableDay(7, 7, 20, 18, 4, 5, 5, None)
    monday.save()

if TimetableDay.get_by_id(53) is None:
    monday = TimetableDay(8, 8, 12, 12, 14, 14, None, None)
    monday.save()

if TimetableDay.get_by_id(54) is None:
    monday = TimetableDay(19, 2, 2, 1, 1, 9, 9, None)
    monday.save()

if TimetableDay.get_by_id(55) is None:
    monday = TimetableDay(9, 9, 13, 3, 5, 9, None, None)
    monday.save()
