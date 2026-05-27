import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User

# Выводим всех пользователей
print("Все пользователи:")
for u in User.objects.all():
    print(f"  - {u.username}")

# Удаляем старого
User.objects.filter(username='admin').delete()

# Создаём заново с простым паролем
User.objects.create_superuser('admin', 'admin@example.com', '123')
print('Админ создан: admin / 123')