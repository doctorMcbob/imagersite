# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
# from django.template import loader


def home_view(request):
    context = {'name': 'world', 'num': 11}
    return render(request, 'home.html', context=context)


def test_view(request, num=0, name=""):
    context = {'num': num, 'name': name}
    return render(request, 'home.html', context=context)


class ClassView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, num=0, name=''):
        return {'num': num, 'name': name}
