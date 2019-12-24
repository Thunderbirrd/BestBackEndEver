from models import Subject

if Subject.get_by_name_and_teacher("Математика", 11) is None:
    math = Subject("subject", "Математика", "", 11, "11")
    math.save()

if Subject.get_by_name_and_teacher("Биология", 1) is None:
    bio = Subject("subject", "Биология", "", 1, "1")
    bio.save()

if Subject.get_by_name_and_teacher("Химия", 2) is None:
    bio = Subject("subject", "Химия", "", 2, "2")
    bio.save()

if Subject.get_by_name_and_teacher("Физика", 3) is None:
    bio = Subject("subject", "Физика", "", 3, "3")
    bio.save()

if Subject.get_by_name_and_teacher("Русский язык", 4) is None:
    bio = Subject("subject", "Русский язык", "", 4, "4")
    bio.save()

if Subject.get_by_name_and_teacher("Литература", 5) is None:
    bio = Subject("subject", "Литература", "", 5, "5")
    bio.save()

if Subject.get_by_name_and_teacher("История", 6) is None:
    bio = Subject("subject", "История", "", 6, "6")
    bio.save()

if Subject.get_by_name_and_teacher("Информатика", 7) is None:
    bio = Subject("subject", "Информатика", "", 7, "7")
    bio.save()

if Subject.get_by_name_and_teacher("Физ-ра", 8) is None:
    bio = Subject("subject", "Физ-ра", "", 8, "8")
    bio.save()

if Subject.get_by_name_and_teacher("Алгебра", 9) is None:
    bio = Subject("subject", "Алгебра", "", 9, "9")
    bio.save()

if Subject.get_by_name_and_teacher("Геометрия", 10) is None:
    bio = Subject("subject", "Геометрия", "", 10, "10")
    bio.save()

if Subject.get_by_name_and_teacher("Англ.яз.", 12) is None:
    bio = Subject("subject", "Англ.яз.", "", 12, "12")
    bio.save()

if Subject.get_by_name_and_teacher("География", 13) is None:
    bio = Subject("subject", "География", "", 13, "13")
    bio.save()

if Subject.get_by_name_and_teacher("Обществознание", 14) is None:
    bio = Subject("subject", "Обществознание", "", 14, "14")
    bio.save()

if Subject.get_by_name_and_teacher("Окружающий мир", 15) is None:
    bio = Subject("subject", "Окружающий мир", "", 15, "15")
    bio.save()

if Subject.get_by_name_and_teacher("ИЗО", 16) is None:
    bio = Subject("subject", "ИЗО", "", 16, "16")
    bio.save()

if Subject.get_by_name_and_teacher("Музыка", 17) is None:
    bio = Subject("subject", "Музыка", "", 17, "17")
    bio.save()

if Subject.get_by_name_and_teacher("ОБЖ", 18) is None:
    bio = Subject("subject", "ОБЖ", "", 18, "18")
    bio.save()

if Subject.get_by_name_and_teacher("Право", 19) is None:
    bio = Subject("subject", "Право", "", 19, "19")
    bio.save()

if Subject.get_by_name_and_teacher("Экономика", 20) is None:
    bio = Subject("subject", "Экономика", "", 20, "20")
    bio.save()

k = 1
for i in range(21, 25):
    if Subject.get_by_name_and_teacher("Окружающий мир", i) is None:
        bio = Subject("subject", "Окружающий мир", "", i, str(i - 20 + k))
        bio.save()
        k += 1

    if Subject.get_by_name_and_teacher("ИЗО", i) is None:
        bio = Subject("subject", "ИЗО", "", i, str(i - 20 + k))
        bio.save()
        k += 1

    if Subject.get_by_name_and_teacher("Музыка", i) is None:
        bio = Subject("subject", "Музыка", "", i, str(i - 20 + k))
        bio.save()
        k += 1

    if Subject.get_by_name_and_teacher("Физ-ра", i) is None:
        bio = Subject("subject", "Физ-ра", "", i, str(i - 20 + k))
        bio.save()
        k += 1

    if Subject.get_by_name_and_teacher("Русский язык", i) is None:
        bio = Subject("subject", "Русский язык", "", i, str(i - 20 + k))
        bio.save()
        k += 1

    if Subject.get_by_name_and_teacher("Литература", i) is None:
        bio = Subject("subject", "Литература", "", i, str(i - 20 + k))
        bio.save()
        k += 1

    if Subject.get_by_name_and_teacher("Математика", i) is None:
        math = Subject("subject", "Математика", "", i, str(i - 20 + k))
        math.save()
        k += 1
