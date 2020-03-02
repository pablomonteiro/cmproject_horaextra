from django.test import TestCase
from django.utils import timezone
from horaextra.models import Registro

# Create your tests here.

def cria_registro(tarefa) :
    return Registro.objects.create(tarefa=tarefa, data=timezone.now(), hora_inicio='09:00', hora_termino='12:00', observacao='teste')

class RegistroTestCase(TestCase) :
    
    def test_deveria_criar_registro (self) :
        cria_registro('VF-123')
        registro = Registro.objects.get(tarefa='VF-123')
        self.assertEqual(registro.tarefa, 'VF-123')