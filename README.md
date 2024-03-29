# CRUD для Yatube
## Описание проекта:
API для нашего проекта Yatube. API должен быть доступен только аутентифицированным пользователям. Используйте в проекте аутентификацию по токену TokenAuthentication. Аутентифицированный пользователь авторизован на изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения. При попытке изменить чужие данные должен возвращаться код ответа 403 Forbidden. В ответ на запросы POST, PUT и PATCH ваш API должен возвращать объект, который был добавлен или изменён.

### Технологии
* Python 3.7.9
* Django 2.2.19
* RestAPI

### Запуск проекта в dev-режиме
* Установите и активируйте виртуальное окружение
* Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
* В папке с файлом manage.py выполните команду:
```
python manage.py runserver(для UNIX - python3 manage.py runserver)
```

### Автор:
Sergey Ragimov
