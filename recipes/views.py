#from django.shortcuts import render

from django.http import HttpResponse
from recipes.models import Recipe

def index(request):
    return HttpResponse("Recipes Index: %d" % Recipe.objects.count())
