from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .models import Material, SitePassword
from .forms import SuggestionForm


def admin_login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('/admin/')
        else:
            return render(request, 'main/admin_login.html', {'error': True})
    return render(request, 'main/admin_login.html')


def check_password(request):
    site_pass = SitePassword.objects.first()
    if not site_pass or not site_pass.password:
        return True
    if request.session.get('access_granted'):
        return True
    return False


def logout_access(request):
    request.session.pop('access_granted', None)
    request.session.pop('welcome_type', None)
    return redirect('index')


def index(request):
    site_pass = SitePassword.objects.first()

    if site_pass and site_pass.password and not request.session.get('access_granted'):
        if request.method == 'POST':
            entered_password = request.POST.get('password', '')
            if entered_password == site_pass.password or entered_password == 'hianton' or entered_password == 'oksana123':
                request.session['access_granted'] = True
                if entered_password == 'hianton':
                    request.session['welcome_type'] = 'father'
                elif entered_password == 'oksana123':
                    request.session['welcome_type'] = 'oksana'
                return redirect('index')
        return render(request, 'main/password.html', {'error': request.method == 'POST'})

    welcome_type = request.session.pop('welcome_type', None)

    references = Material.objects.filter(material_type='reference')
    works = Material.objects.filter(material_type='work')
    lessons = Material.objects.filter(material_type='interactive')
    guides = Material.objects.filter(material_type='classroom')
    return render(request, 'main/index.html', {
        'references': references,
        'works': works,
        'lessons': lessons,
        'guides': guides,
        'welcome_type': welcome_type,
    })


def material_detail(request, pk):
    if not check_password(request):
        return redirect('index')
    material = get_object_or_404(Material, pk=pk)
    return render(request, 'main/material_detail.html', {'material': material})


def add_suggestion(request):
    if not check_password(request):
        return redirect('index')
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
        return redirect('index')
    lessons = Material.objects.filter(material_type='interactive')
    return render(request, 'main/interactive_lessons.html', {'lessons': lessons})


def classroom_guides(request):
    if not check_password(request):
        return redirect('index')
    guides = Material.objects.filter(material_type='classroom')
    return render(request, 'main/classroom_guides.html', {'guides': guides})