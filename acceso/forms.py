from django import forms



class loginform(forms.Form):
	  username=forms.CharField(label="username",required=True)
	  password=forms.CharField(label="contraseña",required=True)




class signupform(forms.Form):
	  username=forms.CharField(label="Username",required=True)
	  password=forms.CharField(label="Password",required=True)
	  email=forms.CharField(label="email",required=True)
	  ubicacion=forms.CharField(label="Username",required=True)