# Cервис управления рассылками, администрирования и получения статистики "Skychimp"
## Описание
* Интерфейс системы содержит следующие экраны:список рассылок, отчет проведенных рассылок отдельно, создание рассылки,
  удаление рассылки, создание пользователя, удаление пользователя, редактирование пользователя.
* При создании рассылки создается задача с периодическими рассылками, которая реализуется с помощью celery и redis.
* Реализовано приложение для ведения блога.
* Права доступа разделены для различных пользователей.
* Модель пользователя расширена для регистрации по почте, а также верификации.
* Настроено кеширование
## Технологии
* Python
* Django
* PostgreSQL
* Celery, Redis
* nginx, gunicorn
* Docker
## Сущности
* Блог
* Клиент
* Сообщение для рассылки
* Рассылка
* Пользователь

### Запуск проекта в Docker:
_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.example:_
```
#Email
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=

#Cache
CACHE_ENABLED=True
CACHES_LOCATION=redis://redis:6379

#Database
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST='db'
POSTGRES_PORT=5432
POSTGRES_HOST_AUTH_METHOD=trust

#Secret_key:
SECRET_KEY=
#Celery
CELERY_BROKER_URL=redis://redis:6379
CELERY_RESULT_BACKEND=redis://redis:6379
```
_Для создания образа из Dockerfile и запуска контейнера запустить команду:_
```
docker-compose up --build
```
_или_
```
docker-compose up -d --build
```
_Второй вариант для запуска в фоновом режиме._
### Запуск приложения в локальной сети:
_Для запуска проекта необходимо клонировать репозиторий, создать и активировать виртуальное окружение:_ 
```
python3 -m venv venv
```
```
source venv/bin/activate
```
_Установить зависимости:_
```
pip install -r requirements.txt
```
_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.sample:_
```
#Email
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
#Cache
CACHE_ENABLED=True
CACHES_LOCATION=redis://localhost:6379

#Database
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432


#Secret_key:
SECRET_KEY=
#Celery
CELERY_BROKER_URL=redis://localhost:6379
CELERY_RESULT_BACKEND=redis://localhost:6379
```
_Для запуска проекта необходимо клонировать репозиторий и создать и активировать виртуальное окружение:_ 
```
python3 -m venv venv
source venv/bin/activate
```
_Установить зависимости:_
```
pip install -r requirements.txt
```
_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.sample_
_Выполнить миграции:_
```
python3 manage.py migrate
```
_Для заполнения БД запустить команду:_
```
python3 manage.py fill
```
_Для создания администратора запустить команду:_
```
python3 manage.py csu
```
_Для заполнения БД запустить команду:_
```
python3 manage.py fill
```
_Для запуска redis_:
```
redis-cli
```
_Для запуска celery:_
```
celery -A config worker --loglevel=info
```
_Для запуска django-celery-beat:_
```
celery -A config beat --loglevel=info
```
_Для запуска приложения:_
```
python3 manage.py runserver
```
