from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import CharField
from acceso.models import Profile

#----------datetime----------------
from datetime import datetime, timedelta
from django.utils import timezone

class Arboles_gen(models.Model):
      tipo=models.CharField(max_length=50)
      regado=models.IntegerField()


      def __str__(self):
          return self.tipo



class Plantados(models.Model):
      arbol_gen=models.ForeignKey(Arboles_gen,on_delete=DO_NOTHING)
      ubi_coord=models.CharField(max_length=100,default="")# le ponemos default para que el serializer no lo pida como obligatorio
      ubi_text=models.CharField(max_length=100)
      ult_regado=models.DateTimeField(auto_now_add=True)
      en_cuidado=models.BooleanField(default=False)
      especificaciones=models.CharField(max_length=200)
      dueño=models.ForeignKey(Profile,on_delete=DO_NOTHING)
      
      def get_ult_regado(self):
          hoy=timezone.now() #el datetime.today() no funciona

          days_dif=(hoy-self.ult_regado)

          return f"{days_dif.days} dias"



      def __str__(self):

          return str(self.id) + ":" + self.arbol_gen.tipo
