from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


# models
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def loginUser(request):
  if request.method == "POST":
    username = request.POST['username']    
    password = request.POST['password']
    
    try:
      user = User.objects.get(username=username)
      print('user in try block', user)
    except:
      print('username does not exist')
    
    newuser = authenticate(request=request, username=username, password=password)
    if newuser is not None:
      login(request, newuser)
      print('newuser: ', newuser)
      return redirect('profiles')
    else:
      print('newuser in else: ', newuser)
      print('user or pass incorrect')
    
  return render(request, 'users/login_register.html')


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