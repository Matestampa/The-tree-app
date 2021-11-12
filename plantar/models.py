from django.db import models
from acceso.models import Profile


class Arboles_gen(models.Model):
      tipo=models.CharField(max_length=50)
      regado=models.IntegerField()


      def __str__(self):
          return self.tipo



class Plantados(models.Model):
      gen_id=models.ForeignKey(Arboles_gen)
      ubi_coord=models.CharField(max_length=100)
      ubi_text=models.CharField(max_length=100)
      ult_regado=models.DateTimeField()
      en_cuidado=models.BooleanField(default=True)
      especificaciones=models.CharField()
      dueño_id=models.ForeignKey(Profile)

      def __str__(self):

          return str(self.id) + ":" + self.gen_id.tipo
