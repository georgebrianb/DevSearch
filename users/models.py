
from django.db import models
from django.contrib.auth.models import User

import uuid

class Profile(models.Model):
  # on_delete=models.CASCADE => everytime a use is deleted, the associated 
  # Profile for that user will also be deleted
  # we will also revert this, so if a profile is deleted => user is deleted 
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=200, blank=True, null=True)
  username = models.CharField(max_length=200, blank=True, null=True)
  location = models.CharField(max_length=200, blank=True, null=True)
  email = models.CharField(max_length=500, blank=True, null=True)
  skills = models.ManyToManyField('Skill', blank=True)
  short_intro = models.CharField(max_length=500, blank=True, null=True)
  bio = models.TextField(blank=True, null=True)
  # for the image, we add a new folder inside static/images/
  # and we add the upload_to field as below
  # a default picture will be used, it will be inside static/images/profiles folder
  profile_image = models.ImageField(blank=True, null=True, upload_to='profiles/', default="profiles/user-default.png")
  social_github = models.CharField(max_length=200, blank=True, null=True)
  social_twitter = models.CharField(max_length=200, blank=True, null=True)
  social_linkedin = models.CharField(max_length=200, blank=True, null=True)
  social_stackoverflow = models.CharField(max_length=200, blank=True, null=True)
  social_website = models.CharField(max_length=200, blank=True, null=True)
  
  
  # auto-generated fields
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  
  def __str__(self):
    return str(self.user.username)
  
  
  
  

class Skill(models.Model):
  owners = models.ManyToManyField(Profile)
  # owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=200, null=True, blank=True)
  description = models.TextField(null=True, blank=True)

  # auto-generated fields
  created = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

  def __str__(self):
    return str(self.name)