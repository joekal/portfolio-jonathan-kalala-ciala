from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html')


def certifications(request):
    return render(request, 'app/certifications.html')


def projets(request):
    return render(request, 'app/projects.html')


def articles(request):
    return render(request, 'app/articles.html')
