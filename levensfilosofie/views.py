from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {'expand_header': True})
