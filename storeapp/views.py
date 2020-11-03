from django.shortcuts import render, HttpResponse

# Create your views here.
from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import *
# Create your views here.

def create_user(request):
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            p = form.cleaned_data.get('permission')
            # print(p)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            u = User.objects.create_user(username = username, password=password)
            u.user_permissions.set(p)
            
            return HttpResponse("Done")
    else:
        form = UserForm()
    context = {'form':form}
    return render(request, 'create_user.html', context)


def add_permission(request):
    if request.method == 'POST':
        pass 
    else:
        permission = Permission.objects.all()
        user = User.objects.all()
        context = {'user':user, 'permission':permission}
        return render(request, 'add_permission.html', context)
