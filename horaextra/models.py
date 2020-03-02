from django.db import models
from django import forms

# Create your models here.

class Registro (models.Model) :
    tarefa = models.CharField(max_length=100)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    observacao = models.TextField()

class RegistroForm (forms.ModelForm) :

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tarefa'].widget.attrs.update({'size':'50'})
        self.fields['data'].widget.attrs.update({'class':'datepicker'})
        self.fields['hora_inicio'].widget.attrs.update({'type': 'time', 'min': '00:00', 'max': '23:59'})
        self.fields['hora_termino'].widget.attrs.update({'type': 'time', 'min': '00:00', 'max': '23:59'})
        self.fields['observacao'].widget.attrs.update({'rows': 3, 'cols': 100})

    class Meta :
        model = Registro
        fields = ['tarefa', 'data', 'hora_inicio', 'hora_termino', 'observacao']