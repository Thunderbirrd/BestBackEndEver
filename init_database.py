from models import Subject

if Subject.get_by_name("математика") is None:
    math = Subject("subject", "математика", "", 1, "1")
    math.save()
