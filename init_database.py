from models import Subject

if Subject.get_by_name("Математика") is None:
    math = Subject("subject", "Математика", "", 11, "11")
    math.save()

if Subject.get_by_name("Биология") is None:
    bio = Subject("subject", "Биология", "", 1, "1")

if Subject.get_by_name("Химия") is None:
    bio = Subject("subject", "Химия", "", 2, "2")


if Subject.get_by_name("Физика") is None:
    bio = Subject("subject", "Физика", "", 3, "3")

if Subject.get_by_name("Русский язык") is None:
    bio = Subject("subject", "Русский язык", "", 4, "4")

if Subject.get_by_name("Литература") is None:
    bio = Subject("subject", "Литература", "", 5, "5")

if Subject.get_by_name("История") is None:
    bio = Subject("subject", "История", "", 6, "6")

if Subject.get_by_name("Информатика") is None:
    bio = Subject("subject", "Информатика", "", 7, "7")

if Subject.get_by_name("Физ-ра") is None:
    bio = Subject("subject", "Физ-ра", "", 8, "8")

if Subject.get_by_name("Алгебра") is None:
    bio = Subject("subject", "Алгебра", "", 9, "9")

if Subject.get_by_name("Геометрия") is None:
    bio = Subject("subject", "Геометрия", "", 10, "10")

if Subject.get_by_name("Англ.яз.") is None:
    bio = Subject("subject", "Англ.яз.", "", 12, "12")

if Subject.get_by_name("География") is None:
    bio = Subject("subject", "География", "", 13, "13")

if Subject.get_by_name("Обществознание") is None:
    bio = Subject("subject", "Обществознание", "", 14, "14")

if Subject.get_by_name("Окружающий мир") is None:
    bio = Subject("subject", "Окружающий мир", "", 15, "15")

if Subject.get_by_name("ИЗО") is None:
    bio = Subject("subject", "ИЗО", "", 16, "16")

if Subject.get_by_name("Музыка") is None:
    bio = Subject("subject", "Музыка", "", 17, "17")

if Subject.get_by_name("ОБЖ") is None:
    bio = Subject("subject", "ОБЖ", "", 18, "18")

if Subject.get_by_name("Право") is None:
    bio = Subject("subject", "Право", "", 19, "19")

if Subject.get_by_name("Экономика") is None:
    bio = Subject("subject", "Экономика", "", 20, "20")

