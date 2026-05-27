from django.shortcuts import render, get_object_or_404, redirect
from .models import Material, SitePassword
from .forms import SuggestionForm


def check_password(request):
    """Проверка пароля перед показом сайта"""
    # Если пароль не задан — пускаем
    site_pass = SitePassword.objects.first()
    if not site_pass:
        request.session['access_granted'] = True
        return None

    # Если уже входил — пускаем
    if request.session.get('access_granted'):
        return None

    # Проверяем пароль из формы
    if request.method == 'POST':
        entered_password = request.POST.get('password', '')
        if entered_password == site_pass.password:
            request.session['access_granted'] = True
            return redirect(request.GET.get('next', 'index'))

    return render(request, 'main/password.html')


def index(request):
    password_check = check_password(request)
    if password_check:
        return password_check

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
    password_check = check_password(request)
    if password_check:
        return password_check

    material = get_object_or_404(Material, pk=pk)
    return render(request, 'main/material_detail.html', {'material': material})


def add_suggestion(request):
    password_check = check_password(request)
    if password_check:
        return password_check

    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SuggestionForm()
    return render(request, 'main/add_suggestion.html', {'form': form})


def interactive_lessons(request):
    password_check = check_password(request)
    if password_check:
        return password_check

    lessons = Material.objects.filter(material_type='interactive')
    return render(request, 'main/interactive_lessons.html', {'lessons': lessons})


def classroom_guides(request):
    password_check = check_password(request)
    if password_check:
        return password_check

    guides = Material.objects.filter(material_type='classroom')
    return render(request, 'main/classroom_guides.html', {'guides': guides})