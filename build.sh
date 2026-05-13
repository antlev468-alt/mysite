#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

# Создаём папки заранее
mkdir -p staticfiles
mkdir -p media

# Собираем статику
python manage.py collectstatic --no-input --clear

# Применяем миграции
python manage.py makemigrations
python manage.py migrate