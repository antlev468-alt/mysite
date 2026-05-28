from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('material/<int:pk>/', views.material_detail, name='material_detail'),
    path('suggestion/', views.add_suggestion, name='add_suggestion'),
    path('lessons/', views.interactive_lessons, name='interactive_lessons'),
    path('classroom/', views.classroom_guides, name='classroom_guides'),
    path('logout/', views.logout_access, name='logout'),
    path('admin-login/', views.admin_login_page, name='admin_login'),
]