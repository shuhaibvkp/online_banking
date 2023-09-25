from django import forms

class reg1form(forms.Form):
    firstname=forms.CharField(max_length=50)
    lastname=forms.CharField(max_length=50)
    username=forms.CharField(max_length=50)
    email=forms.EmailField()
    phone=forms.IntegerField()
    file=forms.FileField()
    pin=forms.CharField(max_length=10)
    pinn=forms.CharField(max_length=10)

class logform(forms.Form):
    username = forms.CharField(max_length=50)
    pin = forms.CharField(max_length=10)

class newsform(forms.Form):
    topic=forms.CharField(max_length=300)
    content=forms.CharField(max_length=3000)

class adminform(forms.Form):
    username=forms.CharField(max_length=30)
    pin=forms.CharField(max_length=30)
