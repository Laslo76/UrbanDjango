from django.shortcuts import render
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = './fourth_task/index.html'


class Basket(TemplateView):
    template_name = './fourth_task/basket_templates.html'


class Shop(TemplateView):
    def get(self, request):
        template = './fourth_task/shop_template.html'
        context = {'products': ['Удочка', 'Поплавок', 'Леска']}
        return render(request, template, context)
