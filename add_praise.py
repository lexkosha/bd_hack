import random

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from datacenter.models import Commendation, Lesson, Schoolkid


def create_commendation(full_name, subject):
    """
    Создает похвалу согласно заданным параметрам
    :param full_name: Передаем ФИО ученика
    :param subject: Передаем предмет
    :return:
    """
    try:
        student = Schoolkid.objects(full_name__contains=full_name).get()
    except ObjectDoesNotExist:
        print('ФИО не найдены в базе')
    except MultipleObjectsReturned:
        print(f'Найдено более одного {full_name}, добавьте фамилию и отчество')
    lesson = Lesson.objects.filter(
        year_of_study=student.year_of_study,
        group_letter=student.group_letter,
        subject__title=subject
    ).first()

    commend_texts = [
        'Сказано здорово – просто и ясно!', 'С каждым разом у тебя получается всё лучше!', 'Страна гордится тобой',
        'Ты будущие России!', 'Не зря тебя мама родила!', f'Ты добился великих достижений по предмету {subject}']
    random_commend = random.choice(commend_text)
    Commendation.objects.create(
        text=random_commend, created=lesson.date,
        schoolkid_id=student.pk, subject_id=lesson.subject_id,
        teacher_id=lesson.teacher.pk)


