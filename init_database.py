from models import Subject

if Subject.get_by_name("Математика") is None:
    math = Subject("subject", "Математика", "", 1, "1")
    math.save()

if Subject.get_by_name("Биология") is None:
    bio = Subject("subject", "Биология", "", 2, "2")

if Subject.get_by_name("Химия") is None:
    bio = Subject("subject", "Химия", "", 3, "3")


if Subject.get_by_name("Физика") is None:
    bio = Subject("subject", "Физика", "", 4, "4")

if Subject.get_by_name("Русский язык") is None:
    bio = Subject("subject", "Русский язык", "", 5, "5")

if Subject.get_by_name("Литература") is None:
    bio = Subject("subject", "Литература", "", 6, "6")

if Subject.get_by_name("История") is None:
    bio = Subject("subject", "История", "", 7, "7")

if Subject.get_by_name("Информатика") is None:
    bio = Subject("subject", "Информатика", "", 8, "8")

if Subject.get_by_name("Физ-ра") is None:
    bio = Subject("subject", "Физ-ра", "", 9, "9")

if Subject.get_by_name("Алгебра") is None:
    bio = Subject("subject", "Алгебра", "", 10, "10")

if Subject.get_by_name("Геометрия") is None:
    bio = Subject("subject", "Геометрия", "", 11, "11")

if Subject.get_by_name("Англ.яз.") is None:
    bio = Subject("subject", "Англ.яз.", "", 12, "12")
