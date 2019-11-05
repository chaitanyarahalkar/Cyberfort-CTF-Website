from django.contrib import admin
from .models import Team,Questions,TeamAdmin, QuestionsAdmin
from django.contrib.sessions.models import Session

admin.site.site_header = 'CyberFort Admin Portal'
admin.site.index_title = 'Adminsitration'
#admin.site.login_template = 'app/admin.html'


# Register your models here.
admin.site.register(Team,TeamAdmin)
admin.site.register(Questions, QuestionsAdmin)
