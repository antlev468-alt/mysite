from django.shortcuts import render, get_object_or_404, redirect
from .models import Material, SitePassword
from .forms import SuggestionForm


def check_password(request):
    """Проверка пароля - возвращает True если доступ разрешён"""
    site_pass = SitePassword.objects.first()

    # Если пароль не задан - пускаем
    if not site_pass or not site_pass.password:
        return True

    # Проверяем сессию
    if request.session.get('access_granted'):
        return True

    # Если пароль введён в текущем запросе
    if request.method == 'POST':
        entered_password = request.POST.get('password', '')
        if entered_password == site_pass.password:
            request.session['access_granted'] = True
            return True

    return False


def index(request):
    site_pass = SitePassword.objects.first()

    # Если пароль задан и нет доступа - показываем форму
    if site_pass and site_pass.password and not check_password(request):
        return render(request, 'main/password.html', {'error': request.method == 'POST'})

    references = Material.objects.filter(material_type='reference')
    works = Material.objects.filter(material_type='work')
    lessons = Material.objects.filter(material_type='interactive')
    guides = Material.objects.filter(material_type='classroom')
    return render(request, 'main/index.html', {
        'references': references,
        'works': works,
        'lessons': lessons,
        'guides': guides,
    })


def material_detail(request, pk):
    if not check_password(request):
        return render(request, 'main/password.html', {'error': request.method == 'POST'})

    material = get_object_or_404(Material, pk=pk)
    return render(request, 'main/material_detail.html', {'material': material})


def add_suggestion(request):
    if not check_password(request):
        return render(request, 'main/password.html', {'error': request.method == 'POST'})

    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SuggestionForm()
    return render(request, 'main/add_suggestion.html', {'form': form})


def interactive_lessons(request):
    if not check_password(request):
        return render(request, 'main/password.html', {'error': request.method == 'POST'})

    lessons = Material.objects.filter(material_type='interactive')
    return render(request, 'main/interactive_lessons.html', {'lessons': lessons})


def classroom_guides(request):
    if not check_password(request):
        return render(request, 'main/password.html', {'error': request.method == 'POST'})

    guides = Material.objects.filter(material_type='classroom')
    return render(request, 'main/classroom_guides.html', {'guides': guides})