from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from sqlalchemy import null
from .models import *
from .forms import PetForm, UserForm

# def home(request, id):
#     profile = User.objects.get(id=id) # profile = get_object_or_404(User, id=id)
#     # pet_profile = Pet.objects.get(user_id = id)
#     if request.method == 'POST':
#         form = UserForm(request.POST, instance = profile)
#         # form_pet = PetForm(request.POST, instance = pet_profile)
#         if form.is_valid():
#             profile = form.save(commit = False)
#             profile.save()

#             # pet_profile = form_pet.save(commit=False)
#             # pet_profile.save()
            
#             return redirect('/'+str(profile.id)+'/', id = profile.id)
#     else:
#         form = UserForm(instance = profile)
#         # form_pet = PetForm(instance = pet_profile)
#         return render(request, 'mypageapp/profile_home.html',
#             {'form':form, 
#             # 'form_pet':form_pet 
#             }
#         )

def home_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            pet_profile = form.save(commit=False)
            pet_profile.save()
            return redirect('mypageapp:pet_list')
        else:
            return redirect('mypageapp:home')
    else:
        form = PetForm()
        return render(request, 'mypageapp/pet_profile.html', {'form':form})
    
    # 임시
def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'mypageapp/pet_list.html', {'pets':pets})

#  def show(request, id):
    pet = get_object_or_404(Pet, pk=id)
    return render(request, 'mypageapp/show.html', {'pet':pet})

def edit(request):
    return render(request,'edit.html')

def pet_profile_update(request, id):
    pet = get_object_or_404(Pet, pk = id)
    if request.method == 'POST':
        form = PetForm(request.POST, instance = pet)
        if form.is_valid:
            pet = form.save(commit = False)
            pet.save()
            return redirect('mypageapp:pet_list') #, id = pet.pk)
    else:
        form = PetForm(instance=pet)
        return render(request, 'mypageapp/pet_profile.html', {'form':form})





def home(request, id):
    profile = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance = profile)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.save()
            return redirect('/'+str(profile.id)+'/', id = profile.id)
    else:
        form = UserForm(instance = profile)
        return render(request, 'mypageapp/profile_home.html',
            {'form':form}
        )