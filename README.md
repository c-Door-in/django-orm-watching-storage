# Security console

Security console website for our bank. You can't launch it without access data from our database.

## How to install
### Install requirements
- Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### Create environment variables
- Create `.env` file in a root directory
- Put connection data in it (replace these values by your own)
```
DB_HOST = YOUR_HOSTNAME
DB_PORT = YOUR_PORTNUMBER
DB_NAME = YOUR_NAME
DB_USER = YOUR_USERNAME
DB_PASSWORD = YOUR_PASSWORD
```
*The service uses Postgres database by default. If you are using another one, you should change `dj-database-url`:*
```
DATABASE_URL = postgres://...
```
See [dj-database-url guide](https://github.com/jacobian/dj-database-url) for details.

- List allowed hosts. Separate them by comma without spaces.
```
DB_ALLOWED_HOSTS = 127.0.0.1,.localhost,.youhost.com
```

## How to start
- Launch the site by using command 
```
python manage.py runserver 0.0.0.0:8000
```

- Go to the site at http://127.0.0.1:8000

## Project purposes

The code was written for a learning — it's a lesson in a Python's and web development course on the site [Devman](https://dvmn.org).

*********************************

# Пульт охраны

Сайт пульта охраны для нашего банка. Вы не сможете запустить его, если у вас нет данных для доступа к нашей базе данных.

## Как установить

### Установка зависимостей
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Создание переменных окружения
- Создайте файл `.env` в корневой директории
- Внесите туда данные для подключения (замените значения на свои)
```
DB_HOST = YOUR_HOSTNAME
DB_PORT = YOUR_PORTNUMBER
DB_NAME = YOUR_NAME
DB_USER = YOUR_USERNAME
DB_PASSWORD = YOUR_PASSWORD
```
*Приложение по-умолчанию использует базу даных Postgres. Если вы используете другую, необходимо поменять `dj-database-url`:*
```
DATABASE_URL = postgres://...
```
Смотрите подробнее на [dj-database-url guide](https://github.com/jacobian/dj-database-url).

- Перечислите разрешенные хосты. Разделите их запятыми без пробелов.
```
DB_ALLOWED_HOSTS = 127.0.0.1,.localhost,.youhost.com
```
## Запуск
- Запустите сайт командой 
```
python manage.py runserver 0.0.0.0:8000
```

- Перейдите на сайт по адресу http://127.0.0.1:8000

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
