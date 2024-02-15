from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.



def index(request, pagename=None, id=None):
    context = {}
    try:
        if (pagename) and (pagename != 'index') and not (str(pagename).__contains__('.html')):
            context['id'] = id
            return render(request, f'{pagename}.html', context=context)
        else:
            context['id'] = id
            return render(request, f'index.html', context=context)
    except Exception as e:
        return HttpResponse(str(e))

