from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import fields

class UserForm(UserCreationForm):

  email = forms.EmailField( required= True )

  class Meta:
    
    model = User
    fields = (
      'username',
      'email',
      'password1',
      'password2'
    )
  
  def __init__(self, *args,  **kwargs):

    super().__init__(*args, **kwargs)

    
    self.fields['username'].widget.attrs.update({'class': 'form-control ms-0 w-100' , 'placeholder' : 'Nombre de usuario'})
    self.fields['email'].widget.attrs.update({'class': 'form-control ms-0 w-100' , 'placeholder' : 'Email'}) 
    self.fields['password1'].widget.attrs.update({'class': 'form-control ms-0 w-100' , 'placeholder' : 'Contraseña'})
    self.fields['password2'].widget.attrs.update({'class': 'form-control ms-0 w-100' , 'placeholder' : 'Repite contraseña'})  
   
    for fieldname in ['username', 'password1', 'password2' , 'email']:
      self.fields[fieldname].label = ''

    for fieldname in ['username', 'password1', 'password2', 'email']:
      self.fields[fieldname].help_text = None
  
  def save(self, commit:True):

    user = super(UserForm, self).save(commit= False)
    user.email = self.cleaned_data['email']

    if commit:
      user.save()
    return user

class UserLoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super(UserLoginForm, self).__init__(*args, **kwargs)
    self.fields['password'].label = ''
    self.fields['username'].label = ''

    self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder' : 'Nombre de usuario'})
    self.fields['password'].widget.attrs.update({'class': 'form-control' , 'placeholder' : 'Contraseña'})
