#!/usr/bin/env bash
set -o errexit

echo "=== Install ==="
pip install -r requirements.txt

echo "=== Dirs ==="
mkdir -p staticfiles media

echo "=== Migrations ==="
python manage.py migrate

echo "=== Static ==="
python manage.py collectstatic --no-input --clear

echo "=== Admin ==="
python create_admin.py