from django.contrib import admin
from .models import project, service,skill

admin.site.register(project)
admin.site.register(service)
admin.site.register(skill)