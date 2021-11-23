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


#class Signup():



@api_view(["POST"])
def login_view(request):
    print(request.data)
    login_instance=Login(request.data)
    
    status=login_instance.validate()
    
    return Response(status)


@api_view(["POST"])
def signup_view(request):
    pass