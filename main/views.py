from django.shortcuts import render, get_object_or_404, redirect
from .models import Material
from .forms import SuggestionForm


def index(request):
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
    material = get_object_or_404(Material, pk=pk)
    return render(request, 'main/material_detail.html', {'material': material})


def add_suggestion(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SuggestionForm()
    return render(request, 'main/add_suggestion.html', {'form': form})


def interactive_lessons(request):
    lessons = Material.objects.filter(material_type='interactive')
    return render(request, 'main/interactive_lessons.html', {'lessons': lessons})


def classroom_guides(request):
    guides = Material.objects.filter(material_type='classroom')
    return render(request, 'main/classroom_guides.html', {'guides': guides})