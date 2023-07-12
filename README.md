Для запуска приложения необходимо настроить виртуальное окружение и установить все необходимые зависимости с помощью команд.

Для запуска celery: celery -A config beat --loglevel=info celery -A config worker --loglevel=info

Для запуска redis: redis-cli

Для заполнения моделей данными необходимо выполнить следующую команду: python3 manage.py fill

Для запуска приложения: python3 manage.py runserver

Для отправки рассылки из командной строки: python3 manage.py sendmessage X, где X - это pk рассылки

Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.sample