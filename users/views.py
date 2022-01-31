from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# models
from django.contrib.auth.models import User
from .models import Profile


def logoutUser(request):
  logout(request)
  messages.error(request, 'User has been logged out')
  return redirect('login')




def loginUser(request):
  if request.user.is_authenticated:
    return redirect('profiles')
  if request.method == "POST":
    print(request.POST)
    username = request.POST['username']    
    password = request.POST['password']
    
    user = authenticate(username=str(username), password=str(password))
    
    
    if user is not None:
      login(request, user)
      return redirect('profiles')
    else:
      messages.error(request, 'Username / Password is incorrect')
    
  return render(request, 'users/login_register.html')


def registerUser(request):
  context = {}
  return render(request, 'users/login_register.html', context) 

def profiles(request):
  profiles = Profile.objects.all()
  context = {'profiles': profiles}
  return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
  profileObj = Profile.objects.get(id=pk)

  # topSkills = [skill for skill in skills if skill.description]
  topSkills = profileObj.skill_set.all().exclude(description__exact="")
  otherSkills = profileObj.skill_set.all().filter(description="")
  context = {
    'profile': profileObj,
    'topSkills': topSkills,
    'otherSkills': otherSkills
  }
  
  return render(request, 'users/user-profile.html', context)