from django.contrib import admin
from .models import Material, Suggestion, SitePassword

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'material_type', 'content_type', 'created_at')
    list_filter = ('material_type', 'content_type')
    search_fields = ('title', 'description')


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('text_preview', 'created_at')

    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Предложение'


@admin.register(SitePassword)
class SitePasswordAdmin(admin.ModelAdmin):
    list_display = ('password',)

    def has_add_permission(self, request):
        # Разрешить добавить только если ещё нет записи
        return not SitePassword.objects.exists()