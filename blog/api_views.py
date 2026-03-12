from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username==username).exists():
        return Response({"error": "Username already exists"}, status=400)
    
    try:  
        validate_password(password)
    except Exception as e:
        return Response({"error": e}, status=400)
    
    user = User.objects.create_user(username=username, password=password)
    return Response({"message": "User created successfully!"}, status=201)

