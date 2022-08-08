# DB_HACK

Скрипт `add_praise.py` добавляет похвалу по заданным параметрам ФИО и уроку.<br> Скрипт добавит похвалу из списка `commend_texts`.

## Пример запуска 
Скрипт кладем в каталог с `manage.py`. Запускаем  в проекте```python manage.py sell``` импортируем скрипт ```from add_praise import create_commendation```.<br> 
Добавляем похвалу  ```create_commendation(full_name='Фролов Иван', subject='Музыка')``` указываем обязательно аргументы ФИО `full_name` и предмет `subject`.

Функция `fix_marks(obj)` принимает объект queryset, исправляет оценки на 5.

Функция `remove_chastisements(schoolkid`) принимает строку 'Голубев Феофан', удаляет все замечания.

## Цели проекта

В образовательных целях в процессе обучения.
