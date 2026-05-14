#!/usr/bin/env bash
set -o errexit

echo "=== Установка зависимостей ==="
pip install -r requirements.txt

echo "=== Создание папок ==="
mkdir -p staticfiles
mkdir -p media

echo "=== Миграции ==="
python manage.py makemigrations main
python manage.py migrate

echo "=== Статика ==="
python manage.py collectstatic --no-input --clear

echo "=== Создание админа ==="
bash create_admin.sh