from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import Contactform

users = {}


def sign_up_by_html(request):
    template_name = './fifth_task/registration_page.html'
    if request.method == 'POST':
        info = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, template_name=template_name, context=info)
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
            return render(request, template_name=template_name, context=info)
        if username in users.keys():
            info['error'] = 'Пользователь уже существует'
            return render(request, template_name=template_name, context=info)
        users[username] = {'password':  password, 'age': age}
        return HttpResponse(f"Приветствуем, {username}!")
    else:
        return render(request, template_name=template_name)


def sign_up_by_django(request):
    template_name = './fifth_task/registration_page.html'
    info = {}
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, template_name=template_name, context=info)
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18 лет'
                return render(request, template_name=template_name, context=info)
            if username in users.keys():
                info['error'] = 'Пользователь уже существует'
                return render(request, template_name=template_name, context=info)
            users[username] = {'password': password, 'age': age}
            return HttpResponse(f"Приветствуем, {username}!")
    else:
        form = Contactform()
    return render(request, template_name, {'form': form})

