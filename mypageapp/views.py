from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import UserForm

def home(request, id):
    profile = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance = profile)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.save()
            return redirect('home', id = profile.id)
    else:
        form = UserForm(instance=profile)
        return render(request, 'mypageapp/profile_home.html',
            {'form':form }
        )