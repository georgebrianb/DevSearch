from django.shortcuts import render
from .models import Profile

# Create your views here.


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