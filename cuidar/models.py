from django.db import models
from django.db.models.deletion import DO_NOTHING


from acceso.models import Profile
from plantar.models import Plantados

class Arbol_cuidador(models.Model):
      id=models.CharField(max_length=100,primary_key=True)
      cuidador=models.ForeignKey(Profile,on_delete=DO_NOTHING)
      arbol=models.ForeignKey(Plantados,on_delete=DO_NOTHING)
      fecha_elegido=models.DateTimeField(auto_now_add=True)


      def __str__(self):
          return f"{cuidador.id}:{arbol.id}"
