#from django.shortcuts import render

from django.http import HttpResponse
from recipes.models import Recipe
from django.template import loader

def index(request):
    template = loader.get_template('recipes/index.html')
    context = {
         'recipes': Recipe.objects.all(),
    }
    return HttpResponse(template.render(context, request))
