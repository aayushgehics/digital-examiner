from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from login.models import LOGIN
from api.serializer import Serializer

@api_view(['GET','POST'])
def login_view(request):
	if(request.method=='GET'):
		login=LOGIN.objects.all()
		serializer=Serializer(LOGIN,many=True)
		return Response(request.data)
	if(request.method=='POST'):
		serializer=Serializer(data=request.data)
		if (serializer.is_valid()):
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
