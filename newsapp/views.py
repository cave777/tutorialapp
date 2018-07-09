from django.shortcuts import render
from tutorial.models import TutorialSeries


def home(request):
    series = TutorialSeries.objects.filter(archived = False).order_by('id')
    template = 'home.html'
    context = {'series':series}
    return render(request, template, context)