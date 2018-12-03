import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

# Forms
from .forms import UserForm

# Models
from .models import User

def index(request):

   form = UserForm(request.POST or None)

   if request.method == 'POST':
      if form.is_valid():
         form.save()

         messages.success(request, 'Added successfully!')
         redirect_url = reverse('main:index')
         return redirect(redirect_url)

   context = {
      'form': form
   }

   return render(request, 'main/index.html', context)

def insert_data(request):
   firstname = request.POST.get('firstname')
   lastname = request.POST.get('lastname')

   try:
      if firstname and lastname:
         new_user = User()
         new_user.firstname = firstname
         new_user.lastname = lastname
         new_user.save()
         data = {
            'msg': True,
         }
   except:
      data = {
         'msg': False,
      }

   dump = json.dumps(data)
   return HttpResponse(dump, content_type='application/json')

def get_data(request):
   user = User.objects.all().count()

   data = {
      'number': user,
   }

   dump = json.dumps(data)
   return HttpResponse(dump, content_type='application/json')
   
