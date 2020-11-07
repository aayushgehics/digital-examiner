from rest_framework import serializers
from login.models import LOGIN
from django.contrib.auth.models import User
class Serializer(serializers.ModelSerializer):
	confirm_password=serializers.CharField(style={'input':'password'},write_only=True)
	class Meta:
		model=User
		fields=['email','username','password','confirm_password']
		context={
		'password':{'write_only':True}
		}
		def save(self):
			model=User(
				email=self.validated_data['email'],
				username=self.validated_data['name'],
				)
			password=self.validated_data['password']
			confirm_password=self.validated_data['confirm_password']
			if (password!=confirm_password):
				raise serializers.ValidationError({'password':'password did not match so try again'})
			else:
				model.set_password('password')
				model.save()
			return model		


		