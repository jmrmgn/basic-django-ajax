from django import forms

from .models import User

class UserForm(forms.ModelForm):
   firstname = forms.CharField(
      label = "Firstname",
      widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter firstname'})
   )

   lastname = forms.CharField(
      label = "Lastname",
      widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lastname'})
   )

   class Meta:
      model = User
      fields = ['firstname', 'lastname']