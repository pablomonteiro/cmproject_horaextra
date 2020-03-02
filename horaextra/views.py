from django.shortcuts import render
from horaextra.models import RegistroForm

# Create your views here.

def add(request) :
    registro = RegistroForm()
    return render(request, 'horaextra/form.html', {'registro': registro})