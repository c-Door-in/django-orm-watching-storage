# Security console

Security console website for our bank. You can't launch it without access data for our database.

## How to install

- Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
- Create `.env` file in a root directory
- Put connection data in it (replace these values to your own)
```
HOST = HOSTNAME
PORT = PORTNUMBER
NAME = NAME
USER = USERNAME
PASSWORD = PASSWORD
```
*The values should be got from module `Django ORM - Lesson 1 on the website` [Devman](https://dvmn.org)*

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

Сайт пульта охраны для нашего банка. Вы не сможете запустить его, если у вас нет данных для доуступа к нашей базе данных.

## Запуск

- Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
- Создайте файл `.env` в корневой директории
- Внесите туда данные для подключения (замените значения на свои)
```
HOST = HOSTNAME
PORT = PORTNUMBER
NAME = NAME
USER = USERNAME
PASSWORD = PASSWORD
```
*Значения необходимо взять из модуля `Урок 1. Пишем пульт охраны банка` на сайте [Devman](https://dvmn.org)*
- Запустите сайт командой 
```
python main.py
```

- Перейдите на сайт по адресу http://127.0.0.1:8000

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
