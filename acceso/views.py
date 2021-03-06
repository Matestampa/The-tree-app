from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User_data, User_access,Profile


class Login():
      def __init__(self,data):
          self.ext_username=data["username"]
          self.ext_password=data["password"]
          #----------------------------------------------------------------------
          self.normal,self.access=User_data,User_access
          self.messages={"1":"Username error","2":"password error","3":"Correcto"}

      def validate(self):
              user=self.check_username()

              if user != "":
                 if self.check_password(user)=="ok":
                    self.status=self.messages["3"]
                 
                 else:
                    self.status=self.messages["2"]
                   
              
              else:
                  self.status=self.messages["1"]
              
              return self.status
              

      def check_password(self,instance):
              real_password=instance.user_access_set.all()[0].password
              if real_password==self.ext_password:
                  return "ok"

              else:
                  return "bad"  


      def check_username(self):
              try:
                  user=self.normal.objects.get(username=self.ext_username)
                  return user
              
              except:
                  return ""


class Signup():
      def __init__(self,data):
          self.data=data
          self.errors={}
      
      def new_error(self,campo,mensaje):
          self.errors[campo]=mensaje
      
      def check_username(self):
          if self.data["username"]!="":
              pass
          
          else:
             self.new_error("Username","El campo username es obligatorio")
      

      def check_password(self):
          if len(self.data["password"])<4:
             self.new_error("Password","Password muy corto")
      

      def check_ubicacion(self):
          if self.data["ubicacion"]!="":
              pass
          
          else:
             self.new_error("Ubicacion","El campo ubicaion no puede estar vacio")



      def is_valid(self):
          self.check_username()
          self.check_password()
          self.check_ubicacion()

          if len(self.errors)!=0:
              return False
          
          else:
              return True
      

      def save(self):
          new_user=User_data.objects.create(username=self.data["username"],email=self.data["email"])
          new_pswd=User_access.objects.create(user=new_user,password=self.data["password"])
          new_profile=Profile.objects.create(user=new_user,ubicacion=self.data["ubicacion"])


      

@api_view(["POST"])
def login_view(request):
    print(request.data)
    login_instance=Login(request.data)
    
    status=login_instance.validate()
    
    return Response(status)



@api_view(["POST"])
def signup_view(request):

    signup_instance=Signup(request.data)

    if signup_instance.is_valid():
       signup_instance.save()

       return Response("Usuario agregado con exito")
    
    else:
        return Response(signup_instance.errors)
       