from datetime import datetime, timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import SignUpSerializer, UserUpSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from .models import Profile



# Create your views here.
@api_view(['POST'])
def register(request):
    data = request.data
    user = SignUpSerializer(data=data)
    
    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            # Create a new user with a random activation token and set account as inactive
            user = User.objects.create_user(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                username=data['email'],
                password=data['password'],
                is_active=True  # Set the user account as inactive initially
            )
            # Generate a random activation token
            activation_token = get_random_string(40)
            expire_date = datetime.now() + timedelta(minutes=30)
            user.profile.activation_token = activation_token
            user.profile.activation_token_expire = expire_date
            user.profile.save()
            print("token", user.profile.activation_token)
            # Construct the activation link
            activation_link = "http://127.0.0.1:8000/api/activate/{activation_token}".format(activation_token=activation_token)
            print("activation link:" , activation_link)
            # Send activation email
            email_subject = "Activate your account on 21 finance"
            email_body = f"Please click the following link to activate your account: {activation_link}"
            send_mail(email_subject, email_body, "21financee@gmail.com", [data['email']])
            
            return Response({'details': 'Account created successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Email already exists!'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def activate_account(request, activation_token):
    print("Activation token received:", activation_token)

    user_profile = get_object_or_404(User, profile__activation_token=activation_token)
    print("User profile:", user_profile)

    if user_profile.profile.activation_token_expire < timezone.now():
        return Response({'error': 'Activation link expired'}, status=status.HTTP_400_BAD_REQUEST)

    print("Activation token expiration:", user_profile.profile.activation_token_expire)

    # Activate the user account
    user_profile.is_active = True
    user_profile.save()

    # Clear activation token and expiration date
    user_profile.profile.activation_token = ""
    user_profile.profile.activation_token_expire = None
    user_profile.profile.save()

    return Response({'details': 'Account activated successfully'}, status=status.HTTP_200_OK)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = SignUpSerializer(request.user, many=False)
    return Response(user.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user
    data = request.data
    user.first_name = data['first_name']
    user.username = data['email']
    user.last_name = data['last_name']
    user.email = data['email']
    
    if data['password'] != "":
        user.password = make_password(data['password'])
    user.save()
    serializer = UserUpSerializer(user, many=False)
    return Response(serializer.data)

def get_current_host(request):
    protocol = request.is_secure() and 'https' or 'http'
    host = request.get_host()
    return "{protocol}://{host}/".format(protocol=protocol, host=host)

@api_view(['POST'])
def forgot_password(request):
    data = request.data
    user = get_object_or_404(User,email=data['email'])
    token = get_random_string(40)
    expire_date = datetime.now() + timedelta(minutes=30)
    user.profile.reset_password_token = token
    user.profile.reset_password_expire = expire_date
    user.profile.save()
    link = "http://127.0.0.1:8000/api/reset_password/{token}".format(token=token)
    body = "Your password reset link is: {link}".format(link=link)
    send_mail(
        "Password Reset from 21 finance",
        body,
        "21financee@gmail.com",
        [data['email']]
    )
    return Response({'details': 'Password reset sent to {email}'.format(email=data['email'])}, status=status.HTTP_200_OK)


@api_view(['POST'])
def reset_password(request, token):
    data = request.data
    user = get_object_or_404(User,profile__reset_password_token = token)
    if user.profile.reset_password_expire.replace(tzinfo=None) < datetime.now():
        return Response({'error': 'Password reset link expired'}, status=status.HTTP_400_BAD_REQUEST)
    
    if data['password'] != data['confirm_password']:
        return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
    user.password = make_password(data['password'])
    user.profile.reset_password_token = ""
    user.profile.reset_password_expire = None
    user.profile.save()
    user.save()
    return Response({'details': 'Password reset done!'}, status=status.HTTP_200_OK)