import random


from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from datacenter.models import Commendation, Lesson, Schoolkid, Chastisement


def create_commendation(full_name, subject):
    """
    Создает похвалу согласно заданным параметрам
    :param full_name: Передаем ФИО ученика
    :param subject: Передаем предмет
    :return:
    """
    try:
        student = Schoolkid.objects.get(full_name__contains=full_name)
        lesson = Lesson.objects.filter(
            year_of_study=student.year_of_study,
            group_letter=student.group_letter,
            subject__title=subject
        ).first()
    except ObjectDoesNotExist:
        print('ФИО не найдены в базе')
    except MultipleObjectsReturned:
        print(f'Найдено более одного {full_name}, добавьте фамилию и отчество')

        commend_text = [
            'Сказано здорово – просто и ясно!', 'С каждым разом у тебя получается всё лучше!', 'Страна гордится тобой',
            'Ты будущие России!', 'Не зря тебя мама родила!', f'Ты добился великих достижений по предмету {subject}'
        ]
        random_commend = random.choice(commend_text)

        Commendation.objects.create(
            text=random_commend, created=lesson.date,
            schoolkid_id=student.pk, subject_id=lesson.subject_id,
            teacher_id=lesson.teacher.pk)


def remove_chastisements(schoolkid):
    student = Schoolkid.objects.get(full_name__contains='Голубев Феофан')
    remarks = Chastisement.objects.filter(schoolkid__id=student.id)
    remarks.delete()


def fix_marks(schoolkid):
    for mark in schoolkid:
        mark.points = 5
        mark.save()
