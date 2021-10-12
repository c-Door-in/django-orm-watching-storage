# Security console

Security console website for our bank. You can't launch it without access data from our database.

## How to install

- Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
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

## Запуск

- Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
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
- Запустите сайт командой 
```
python main.py
```

- Перейдите на сайт по адресу http://127.0.0.1:8000

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
