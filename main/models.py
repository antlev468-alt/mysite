from django.db import models


class Material(models.Model):
    MATERIAL_TYPES = (
        ('reference', 'Справочник'),
        ('work', 'Учебная работа'),
        ('interactive', 'Интерактивный урок'),
        ('classroom', 'Классное руководство'),
    )

    CONTENT_TYPES = (
        ('link', 'Ссылка'),
        ('text', 'Текст'),
        ('photo', 'Фото'),
        ('file', 'Файл'),
    )

    title = models.CharField(max_length=200, verbose_name='Название')
    material_type = models.CharField(
        max_length=20, choices=MATERIAL_TYPES, verbose_name='Тип материала'
    )
    content_type = models.CharField(
        max_length=10, choices=CONTENT_TYPES, default='link',
        verbose_name='Тип содержимого'
    )
    external_url = models.URLField(blank=True, verbose_name='Ссылка')
    text_content = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to='materials/', blank=True, verbose_name='Фото')
    file = models.FileField(upload_to='files/', blank=True, verbose_name='Файл')
    description = models.TextField(blank=True, verbose_name='Краткое описание')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    def __str__(self):
        return self.title


class Suggestion(models.Model):
    text = models.TextField(verbose_name='Текст предложения')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

    def __str__(self):
        return f'Предложение от {self.created_at:%d.%m.%Y %H:%M}'