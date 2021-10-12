from django.shortcuts import render
from .models import User_data, User_access
from .forms import loginform, signupform
# Create your views here.


def login(request):
    login_form=loginform()

    if request.method=="GET":

        return render(request,"login.html",{"login_form":login_form})

    if request.method=="POST":
       data_recv=request.POST
       
       user=User_data.objects.get(username=data_recv["username"])
       
       user_login=user.user_access_set.all()[0]
       print(user_login)
       
       if data_recv["password"]==user_login.password:
          request.session["id"]=user.id
          
          return redirect("/home")

       else:
          error="Contraseña incorrecta"
          return render(request,"login.html",{"login_form":login_form,"error":error})






def signup(request):
    signup_form=signupform()
    if request.method=="GET":

       return render(request,"signup.html",{"signup_form":signup_form})

    if request.method=="POST":
        data_recv=request.POST

        if len(data_recv["password"])<4:
            
            error="Contraseña muy corta"
            
            return render(request,"signup.html",{"signup_form":signup_form,"error":error})
        
        #---------------meter los nuevos datos------------------
        new_user=User_data(username=data_recv["username"])
        new_user.save()

        access_data=User_access(user=new_user,password=data_recv["password"],numero=data_recv["numero"])
        access_data.save()

        profile_data=Profile(user=new_user,edad=data_recv["edad"])
        profile_data.save()

        #-------------------------------------------------------
        
        request.session["id"]=new_user.id
        return redirect("/home")
