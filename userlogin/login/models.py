from django.db import models

# Create your models here.
class LOGIN(models.Model):
	email=models.EmailField()
	username=models.CharField(max_length=120)
	password=models.CharField(default='aa',max_length=120)
	confirm_password=models.CharField(default='aa',max_length=120)
