from django.db import migrations
from django.contrib.auth.models import User

def create_admin(apps, schema_editor):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'antlev468@gmail.com', 'admin123456')

class Migration(migrations.Migration):
    dependencies = [
        ('main', '0003_material_content_type_material_photo_and_more'),
    ]

    operations = [
        migrations.RunPython(create_admin),
    ]