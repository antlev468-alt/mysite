import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='oksana').exists():
    User.objects.create_superuser('oksana', 'admin@example.com', 'oksana123')
    print('oksana / oksana123')

if not User.objects.filter(username='anton').exists():
    User.objects.create_superuser('anton', 'hianton@example.com', 'hianton')
    print('anton / hianton')