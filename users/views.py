from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


# models
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def loginUser(request):
  if request.user.is_authenticated:
    return render(request, '')
  if request.method == "POST":
    print(request.POST)
    username = request.POST['username']    
    # password = request.POST['password']
    password = request.POST.get('password')
    print('pass:', password)
    # try:
    #   user = User.objects.get(username=username)
    #   print('user in try block', user)
    # except:
    #   print('username does not exist')
    
    user = authenticate(username=str(username), password=str(password))
    
    
    if user is not None:
      login(request, user)
      print('newuser: ', user)
      return redirect('profiles')
    else:
      print('newuser in else: ', user)
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