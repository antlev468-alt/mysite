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
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'Admin123456!') if not User.objects.filter(username='admin').exists() else print('admin exists')" | python manage.py shell

echo "=== ГОТОВО ==="