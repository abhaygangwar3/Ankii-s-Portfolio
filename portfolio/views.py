from django.shortcuts import render
from .models import PortfolioModel


def homepage(request):

    project = PortfolioModel.objects.all()
    return render(request, 'portfolio/homepage.html', {'projects': project})