from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.


class project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images/projects", default = "images/gallery/gallery-1.jpg")
    active = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=True)
    
   
    def __str__(self):
        return self.title
    

class service(models.Model):
    title = models.CharField(max_length=100)
    Description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
  
    
class skill(models.Model):
    skill = CharField(max_length= 100)
    skill_icon = ImageField(null=True, blank=True, upload_to='images/skill-icon', default='images/about-img.png')
    
    def __str__(self):
        return self.skill