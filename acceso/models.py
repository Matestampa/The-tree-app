from django.db import models

# Create your models here.

class User_data(models.Model):
	   username=models.CharField(max_length=50,unique=True)
	   email=models.CharField(max_length=80)


	   def __str__(self):
	   	   return self.username


class User_access(models.Model):
	  user_id=models.ForeignKey(User_data,on_delete=models.CASCADE)
	  password=models.CharField(max_length=50)

	  def __str__(self):
	  	  return str(self.id) + " : " + self.user_id.username