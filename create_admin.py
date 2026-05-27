import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User

# Админ
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', '123')
    print('admin / 123')

# Особый пользователь
if not User.objects.filter(username='hianton').exists():
    User.objects.create_superuser('hianton', 'hianton@example.com', 'hianton')
    print('hianton / hianton')