from models import TimetableDay

if TimetableDay.get_by_id(1) is None:
    monday = TimetableDay(13, 4, 8, 11, None, None, None, None)
    monday.save()
