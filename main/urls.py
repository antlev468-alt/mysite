from django.shortcuts import render, get_object_or_404, redirect
from .models import Material, SitePassword
from .forms import SuggestionForm


def check_password(request):
    site_pass = SitePassword.objects.first()

    if not site_pass or not site_pass.password:
        return True

    if request.session.get('access_granted'):
        return True

    if request.method == 'POST':
        entered_password = request.POST.get('password', '')
        if entered_password == site_pass.password or entered_password == 'hianton':
            request.session['access_granted'] = True
            if entered_password == 'hianton':
                request.session['show_welcome'] = True
            return True

    return False


def index(request):
    site_pass = SitePassword.objects.first()

    if site_pass and site_pass.password and not check_password(request):
        return render(request, 'main/password.html', {'error': request.method == 'POST'})

    show_welcome = request.session.pop('show_welcome', False)

    references = Material.objects.filter(material_type='reference')
    works = Material.objects.filter(material_type='work')
    lessons = Material.objects.filter(material_type='interactive')
    guides = Material.objects.filter(material_type='classroom')
    return render(request, 'main/index.html', {
        'references': references,
        'works': works,
        'lessons': lessons,
        'guides': guides,
        'show_welcome': show_welcome,
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