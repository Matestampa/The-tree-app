from rest_framework.decorators import api_view
from rest_framework. response import Response
from rest_framework import status

from rest_framework import generics

#------------serializers---------------
from plantar.serializers import Trees_Serializer

#------------models-----------------------
from acceso.models import Profile, User_data
from plantar.models import Plantados
from cuidar.models import Arbol_cuidador

def make_id(user,arbol):
	return "{}{}".format(user,arbol)



class Cuidar_tree():
	  def __init__(self,data):
		  self.data=data
		  self.cuidador=data["user"]
		  self.arbol=data["arbol"]
	  

	  def create(self):
		  self.data["id"]=make_id(self.cuidador,self.arbol)
		  
		  cuidador=Profile.objects.get(id=self.cuidador)

		  arbol=Plantados.objects.get(id=self.arbol)
	
		  Arbol_cuidador.objects.create(id=self.data["id"],cuidador=cuidador,arbol=arbol)

		  arbol.en_cuidado=True
		  arbol.save()

		  



@api_view(["GET"])
def all_trees(request):
	trees=Plantados.objects.filter(en_cuidado=False)
    
	serialized_trees=Trees_Serializer(trees,many=True)

	return Response(serialized_trees.data)


@api_view(["POST"])
def take_tree(request):
	if User_data.objects.filter(id=request.data["user"]).count()==0:
		return Response("Usuario no existente",status=status.HTTP_400_BAD_REQUEST)
	
	else:
		instance=Cuidar_tree(request.data)
		instance.create()

		return Response("Registro añadido",status=status.HTTP_201_CREATED)



@api_view(["POST"])
def confirm(request):
    
	id=make_id(request.data["user"],request.data["arbol"])
	
	try:
	    Arbol_cuidador.objects.get(id=id).delete()
	    arbol=Plantados.objects.get(id=request.data["arbol"])
	    arbol.en_cuidado=False
	    arbol.save()
	    return Response("confirmacion realizada",status=status.HTTP_202_ACCEPTED)
	
	except:
		return Response("Id no valido",status=status.HTTP_400_BAD_REQUEST)







"""setear en_cuidado=True
	generar nuevo registro,(hacer lo del id manual)
	si confirma:
		seteamos en_cuidado=False
		se actualiza la fecha
		
	sino:
		vemos como poronga poner el timer"""

		

