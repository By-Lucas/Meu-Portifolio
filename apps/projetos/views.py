from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def recursos(request):
    return render(request, 'recursos.html')


def beneficios(request):
    return render(request, 'beneficios.html')


def precos(request):
    return render(request, 'precos.html')
