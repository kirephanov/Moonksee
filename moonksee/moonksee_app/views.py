from django.shortcuts import render


def index(request):
    return render(request=request, template_name='moonksee_app/index.html', context={'title': 'Moonksee'})
