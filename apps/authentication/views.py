from django.shortcuts import render
from rest_framework import views, generics, permissions, status
from rest_framework.response import Response

#local imports
from apps.authentication.serializers import ProfileSerializer, UserSerializer, RegisterSerializer, LoginSerializer
from apps.authentication.models import Profile
from apps.authentication.exceptions import ProfileNotFound
# third party imports
from knox.models import AuthToken

# Create your views here.

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user)
        user.save()
        token = AuthToken.objects.create(user)
        return Response({
            "users": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token[1]
        }, status=status.HTTP_200_OK)

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.get_serializer(data=serializer.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({
            "users": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token[1]
        }, status=status.HTTP_200_OK)

class UserAPI(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = ( 
        permissions.IsAuthenticated,
    )
    def get(self,request):
        user = self.request.user 
        try: 
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            raise ProfileNotFound
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)



