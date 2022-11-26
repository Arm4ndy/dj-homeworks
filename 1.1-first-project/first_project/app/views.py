from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
from os import listdir,path
from app import __file__ as curr_dir_path


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.utcnow().strftime("%d-%m-%Y %H:%M")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    curr_dir = listdir(path.dirname(curr_dir_path))
    return HttpResponse('<br>'.join(curr_dir))
