from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def detail(request, artikel=1):
    context = {
        'artikelnr': artikel
    }
    return render(request, 'detail.html', context=context)
