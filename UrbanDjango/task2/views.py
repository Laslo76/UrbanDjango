from django.shortcuts import render
from django.views.generic import TemplateView


class task2(TemplateView):
    template_name = './second_task/class_template.html'


# Create your views here.
def task2_func(request):
    return render(request, './second_task/func_templates.html')
