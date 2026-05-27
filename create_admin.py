import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User

# Удаляем старого админа
User.objects.filter(username='admin').delete()

# Создаём нового
User.objects.create_superuser('admin', 'antlev468@gmail.com', 'Pass123!')
print('Superuser created!')