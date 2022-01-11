from django import template
from django.core.mail.message import EmailMessage
from django.forms.forms import Form
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import project, skill

from .form import PostForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

    
def index(request):
   skills = skill.objects.all()
   projects = project.objects.filter(active = True, )[0:1]
   context = {'projects': projects, 'skills':skills}
   return render(request, 'base/index.html', context)

def posts(request):
    projects = project.objects.filter(active = True)
    context = {'projects': projects}
    return render(request, 'base/posts.html', context)


def post(request, pk):
    Project = project.objects.get(id = pk)
    context = {'project': Project}
    return render(request, 'base/post.html', context)

def profile(request):
    return render(request, 'base/profile.html')

#CRUD

def createpost(request):
    form = PostForm()
    context = {'form':form}
    return render(request, 'base/post_form.html', context)

def sendEmail(request):
    template = render_to_string('base/email_template.html',{
        'name' : request.POST['name'],
        'email' : request.POST['email'],
        'message': request.POST['message']
    })
    eamil = EmailMessage(
        request.POST['subject'],
        template, 
        settings.EMAIL_HOST_USER,['webracket.dev@gmail.com']
        
    )
    eamil.fail_silent = False
    eamil.send()
    return render(request, "base/email_sent.html")