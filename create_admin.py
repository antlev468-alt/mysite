import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User

# Удаляем старого админа если есть
User.objects.filter(username='admin').delete()

# Создаём нового
User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='Admin123456!'
)
print('АДМИН СОЗДАН!')