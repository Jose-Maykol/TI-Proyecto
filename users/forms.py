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

    """ 
    Para modificar la clase de los fields de formulario
    self.fields['email'].widget.attrs.update({'class': '' , 'placeholder' : ''}) 
    """
  
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
