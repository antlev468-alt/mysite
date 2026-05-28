#!/usr/bin/env bash
set -o errexit

echo "=== Install ==="
pip install -r requirements.txt

echo "=== Dirs ==="
mkdir -p staticfiles media

echo "=== Clear sessions ==="
rm -f db.sqlite3
python manage.py migrate
python manage.py makemigrations main
python manage.py migrate

echo "=== Create admin ==="
python create_admin.py

echo "=== Static ==="
python manage.py collectstatic --no-input --clear