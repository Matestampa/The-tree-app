from django.db import models

# Create your models here.


###### PENSAR EN EL MANEJO DE LOS IDS ###################################
class User_data(models.Model):
	   username=models.CharField(max_length=50,unique=True)
	   email=models.CharField(max_length=80)


	   def __str__(self):
	   	   return self.username


class User_access(models.Model):
	  password=models.CharField(max_length=50)
	  user=models.ForeignKey(User_data,on_delete=models.CASCADE)

	  def encrypt_pswd(text):
		  pass

	  def __str__(self):
	  	  return str(self.id) + " : " + self.user.username


class Profile(models.Model):
	  ubicacion=models.CharField(max_length=100)
	  foto=models.CharField(max_length=100)
	  user=models.ForeignKey(User_data,on_delete=models.CASCADE)
	  
	  def __str__(self):
	      return str(self.user.id) + ":" + self.user.username