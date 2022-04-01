# python_libs_catalog
##### _разработка Sayfullin R.R.


Cервис терминологии и REST API к нему

Документация API (автодокументирование на swagger (drf-yasg) доступно по адресу http://127.0.0.1:8000/swagger/ )

========================================================================================================================
#Описание ТЗ:

Сервис терминологии оперирует ниже перечисленными сущностями.



Сущность "Справочник" содержит следующие атрибуты:

- идентификатор справочника (глобальный и не зависит от версии)
- наименование
- короткое наименование
- описание
- версия (тип: строка,  не может быть пустойуникальная в пределах одного справочника)
- дата начала действия справочника этой версии



Сущность "Элемент справочника"

- идентификатор
- родительский идентификатор
- код элемента (тип: строка, не может быть пустой)
- значение элемента (тип: строка, не может быть пустой)



API должно предоставлять следующие методы:

- получение списка справочников.
- получение списка справочников, актуальных на указанную дату.
- получение элементов заданного справочника текущей версии
- валидация элементов заданного справочника текущей версии
- получение элементов заданного справочника указанной версии
- валидация элемента заданного справочника по указанной версии

В API должен быть предусмотрен постраничный вывод результата (данные должны возвращаться частями по 10 элементов).

К сервису должна иметься GUI административной части, с помощью которой можно добавлять новые справочники, новые версии справочников, указывать дату начала действия и наполнять справочники элементами.

Некоторые подробности намеренно не указаны. Оставляем их на ваше усмотрение.

## Технологии

* Python >= 3.8

## Критерии оценки

* Выполнение требований ТЗ.
* Читаемость программного кода (отступы, разделители и т.д.).
* Адекватность выбора подхода: технологий, конструкций языка.
* Наличие в коде программы комментариев и их содержание.
* Невозможность внесения некорректных данных пользователем.
* Наличие ошибок в программе (не ожиданное поведение, не корректные выходные данные), в том числе возникающих при непредусмотренных действиях пользователей.
* Удобство использования (логичность элементов API и GUI-интерфейса).
* Наличие описания разработанного API с примерами.
========================================================================================================================
Протестировано на ОС Debian 11

Склонируйте репозиторий с помощью git:
https://github.com/RuslanSayfullin/python_libs_catalog.git

Перейти в папку:
$ cd python_libs_catalog

создайте изолированное окружение с помощью команды:
python3 -m venv venv

после активации виртуального окружения выполнить команду:
source venv/bin/activate

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```
========================================================================================================================
Выполнить следующие команды:

Перейти в папку:
$ cd catalog

    Команда для создания миграций приложения для базы данных

python3 manage.py makemigrations
python3 manage.py migrate

    Создание суперпользователя

python3 manage.py createsuperuser

Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту и пароль: по умолчанию почта admin@admin.com пароль: 12345

Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.

    Команда для запуска приложения

python manage.py runserver

    Приложение будет доступно по адресу: http://127.0.0.1:8000/
