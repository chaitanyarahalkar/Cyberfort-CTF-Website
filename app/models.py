from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin


# Create your models here. Use set_password 
JUNIOR = 'JR'
SENIOR = 'SR'
CATEGORY_CHOICE = ((JUNIOR,'Junior'),(SENIOR,'Senior'))

class Team(AbstractUser):
	email1 = models.EmailField()
	email2 = models.EmailField(default='johndoe@example.com')
	phone1 = models.IntegerField(default=0)
	phone2 = models.IntegerField(default=0)
	points = models.IntegerField(default=0)
	category = models.CharField(max_length=2,choices=CATEGORY_CHOICE,default=JUNIOR)
	timeRequired = models.FloatField(default=0)
	played = models.BooleanField(default=False)

	def convert(self):
		return '{}:{}'.format(int(self.timeRequired//60),int(self.timeRequired%60))

	def __str__(self):
		return self.username


class TeamAdmin(admin.ModelAdmin):
	list_display = ('username','category','timeRequired','points')
	readonly_fields = ('password','points','timeRequired')
	search_fields = ['username','timeRequired','points','email1','email2']


class Questions(models.Model):
	questionId = models.IntegerField(default=0)
	questionDescription = models.TextField()
	questionPoints = models.IntegerField(default=0)
	questionCategory = models.CharField(max_length=2,choices=CATEGORY_CHOICE,default=JUNIOR)
	questionData = models.FileField(blank=True)
	questionFlag = models.CharField(max_length=50,default='pict_CTF{}')
	questionHint = models.TextField(default="Sample Hint")
	questionSolvers = models.IntegerField(default=0)


	def __str__(self):
		return self.questionDescription

	class Meta:
		verbose_name = 'Question'
		verbose_name_plural = 'Questions'


class QuestionsAdmin(ImportExportActionModelAdmin):
	pass