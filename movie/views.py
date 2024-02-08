from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'name':'Alfonso'})
def about(request):
    return HttpResponse('<h1>Nya uwu</h1>')