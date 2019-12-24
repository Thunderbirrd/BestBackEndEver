from models import Subject

if Subject.get_subject("Математика", 11, "5a") is None:
    math = Subject("subject", "Математика", "", 11, "11", "5a")
    math.save()

if Subject.get_subject("Биология", 1, "5a") is None:
    bio = Subject("subject", "Биология", "", 1, "1", "5a")
    bio.save()

if Subject.get_subject("Химия", 2, "5a") is None:
    bio = Subject("subject", "Химия", "", 2, "2", "5a")
    bio.save()

if Subject.get_subject("Физика", 3, "5a") is None:
    bio = Subject("subject", "Физика", "", 3, "3", "5a")
    bio.save()

if Subject.get_subject("Русский язык", 4, "5a") is None:
    bio = Subject("subject", "Русский язык", "", 4, "4", "5a")
    bio.save()

if Subject.get_subject("Литература", 5, "5a") is None:
    bio = Subject("subject", "Литература", "", 5, "5", "5a")
    bio.save()

if Subject.get_subject("История", 6, "5a") is None:
    bio = Subject("subject", "История", "", 6, "6", "5a")
    bio.save()

if Subject.get_subject("Информатика", 7, "5a") is None:
    bio = Subject("subject", "Информатика", "", 7, "7", "5a")
    bio.save()

if Subject.get_subject("Физ-ра", 8, "5a") is None:
    bio = Subject("subject", "Физ-ра", "", 8, "8", "5a")
    bio.save()

if Subject.get_subject("Алгебра", 9, "5a") is None:
    bio = Subject("subject", "Алгебра", "", 9, "9", "5a")
    bio.save()

if Subject.get_subject("Геометрия", 10, "5a") is None:
    bio = Subject("subject", "Геометрия", "", 10, "10", "5a")
    bio.save()

if Subject.get_subject("Англ.яз.", 12, "5a") is None:
    bio = Subject("subject", "Англ.яз.", "", 12, "12", "5a")
    bio.save()

if Subject.get_subject("География", 13, "5a") is None:
    bio = Subject("subject", "География", "", 13, "13", "5a")
    bio.save()

if Subject.get_subject("Обществознание", 14, "5a") is None:
    bio = Subject("subject", "Обществознание", "", 14, "14", "5a")
    bio.save()

if Subject.get_subject("Окружающий мир", 15, "5a") is None:
    bio = Subject("subject", "Окружающий мир", "", 15, "15", "5a")
    bio.save()

if Subject.get_subject("ИЗО", 16, "5a") is None:
    bio = Subject("subject", "ИЗО", "", 16, "16", "5a")
    bio.save()

if Subject.get_subject("Музыка", 17, "5a") is None:
    bio = Subject("subject", "Музыка", "", 17, "17", "5a")
    bio.save()

if Subject.get_subject("ОБЖ", 18, "5a") is None:
    bio = Subject("subject", "ОБЖ", "", 18, "18", "5a")
    bio.save()

if Subject.get_subject("Право", 19, "5a") is None:
    bio = Subject("subject", "Право", "", 19, "19", "5a")
    bio.save()

if Subject.get_subject("Экономика", 20, "5a") is None:
    bio = Subject("subject", "Экономика", "", 20, "20", "5a")
    bio.save()

k = 1
for i in range(21, 25):
    if Subject.get_subject("Окружающий мир", i, str(i - 20) + "a") is None:
        bio = Subject("subject", "Окружающий мир", "", i, str(20 + k), str(i - 20) + "a")
        bio.save()
        k += 1

    if Subject.get_subject("ИЗО", i, str(i - 20) + "a") is None:
        bio = Subject("subject", "ИЗО", "", i, str(20 + k), str(i - 20) + "a")
        bio.save()
        k += 1

    if Subject.get_subject("Музыка", i, str(i - 20) + "a") is None:
        bio = Subject("subject", "Музыка", "", i, str(20 + k), str(i - 20) + "a")
        bio.save()
        k += 1

    if Subject.get_subject("Физ-ра", i, str(i - 20) + "a") is None:
        bio = Subject("subject", "Физ-ра", "", i, str(20 + k), str(i - 20) + "a")
        bio.save()
        k += 1

    if Subject.get_subject("Русский язык", i, str(i - 20) + "a") is None:
        bio = Subject("subject", "Русский язык", "", i, str(20 + k), str(i - 20) + "a")
        bio.save()
        k += 1

    if Subject.get_subject("Литература", i, str(i - 20) + "a") is None:
        bio = Subject("subject", "Литература", "", i, str(20 + k), str(i - 20) + "a")
        bio.save()
        k += 1

    if Subject.get_subject("Математика", i, str(i - 20) + "a") is None:
        math = Subject("subject", "Математика", "", i, str(20 + k), str(i - 20) + "a")
        math.save()
        k += 1

for i in range(6, 12):
    if Subject.get_subject("Математика", 11, str(i) + "a") is None:
        math = Subject("subject", "Математика", "", 11, "11", str(i) + "a")
        math.save()

    if Subject.get_subject("Биология", 1, str(i) + "a") is None:
        bio = Subject("subject", "Биология", "", 1, "1", str(i) + "a")
        bio.save()

    if Subject.get_subject("Химия", 2, str(i) + "a") is None:
        bio = Subject("subject", "Химия", "", 2, "2", str(i) + "a")
        bio.save()

    if Subject.get_subject("Физика", 3, str(i) + "a") is None:
        bio = Subject("subject", "Физика", "", 3, "3", str(i) + "a")
        bio.save()

    if Subject.get_subject("Русский язык", 4, str(i) + "a") is None:
        bio = Subject("subject", "Русский язык", "", 4, "4", str(i) + "a")
        bio.save()

    if Subject.get_subject("Литература", 5, str(i) + "a") is None:
        bio = Subject("subject", "Литература", "", 5, "5", str(i) + "a")
        bio.save()

    if Subject.get_subject("История", 6, str(i) + "a") is None:
        bio = Subject("subject", "История", "", 6, "6", str(i) + "a")
        bio.save()

    if Subject.get_subject("Информатика", 7, str(i) + "a") is None:
        bio = Subject("subject", "Информатика", "", 7, "7", str(i) + "a")
        bio.save()

    if Subject.get_subject("Физ-ра", 8, str(i) + "a") is None:
        bio = Subject("subject", "Физ-ра", "", 8, "8", str(i) + "a")
        bio.save()

    if Subject.get_subject("Алгебра", 9, str(i) + "a") is None:
        bio = Subject("subject", "Алгебра", "", 9, "9", str(i) + "a")
        bio.save()

    if Subject.get_subject("Геометрия", 10, str(i) + "a") is None:
        bio = Subject("subject", "Геометрия", "", 10, "10", str(i) + "a")
        bio.save()

    if Subject.get_subject("Англ.яз.", 12, str(i) + "a") is None:
        bio = Subject("subject", "Англ.яз.", "", 12, "12", str(i) + "a")
        bio.save()

    if Subject.get_subject("География", 13, str(i) + "a") is None:
        bio = Subject("subject", "География", "", 13, "13", str(i) + "a")
        bio.save()

    if Subject.get_subject("Обществознание", 14, str(i) + "a") is None:
        bio = Subject("subject", "Обществознание", "", 14, "14", str(i) + "a")
        bio.save()

    if Subject.get_subject("Окружающий мир", 15, str(i) + "a") is None:
        bio = Subject("subject", "Окружающий мир", "", 15, "15", str(i) + "a")
        bio.save()

    if Subject.get_subject("ИЗО", 16, str(i) + "a") is None:
        bio = Subject("subject", "ИЗО", "", 16, "16", str(i) + "a")
        bio.save()

    if Subject.get_subject("Музыка", 17, str(i) + "a") is None:
        bio = Subject("subject", "Музыка", "", 17, "17", str(i) + "a")
        bio.save()

    if Subject.get_subject("ОБЖ", 18, str(i) + "a") is None:
        bio = Subject("subject", "ОБЖ", "", 18, "18", str(i) + "a")
        bio.save()

    if Subject.get_subject("Право", 19, str(i) + "a") is None:
        bio = Subject("subject", "Право", "", 19, "19", str(i) + "a")
        bio.save()

    if Subject.get_subject("Экономика", 20, str(i) + "a") is None:
        bio = Subject("subject", "Экономика", "", 20, "20", str(i) + "a")
        bio.save()
