from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from registration.models import reg_table

# Create your views here.
def home(request):
      name='Malilo'
      context={'name':name}
      return render(request,'home.html',context)
def register(request):
      registered=False
      form=UserCreationForm()
      if request.method=='POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                  form.save()
                  registered=True
                  context={'success':'Successfull registered','registered':registered}
                  return render(request,'home.html',context)
      context={'form':form}
      return render(request,'register.html',context)
def display(request):
      users=reg_table.objects.all()
      context={'userlist':users}
      return render(request,'display.html',context)
