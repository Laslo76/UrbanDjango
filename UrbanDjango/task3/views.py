from django.shortcuts import render
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = './third_task/index.html'


class Basket(TemplateView):
    template_name = './third_task/basket_templates.html'


class Shop(TemplateView):
    def get(self, request):
        template = './third_task/shop_template.html'
        context = {'prod1': 'Удочка',
                   'prod2': 'Поплавок',
                   'prod3': 'Леска'}
        return render(request, template, context)
