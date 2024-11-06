from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer


class UserCreateApiView(APIView):
  def get_permissions(self):
    if self.request.method == 'POST':
      return [AllowAny()]
    return [IsAuthenticated()]

  def post(self, request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      return Response(UserSerializer(user).data, status=status.Http_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileUpdateApiView(APIView):
  permission_classes = [IsAuthenticated]

  def put(self, request, pk=None):
    try:
      user = User.objects.get(pk=pk)
    except User.DoesNotExist:
      return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    profile = user.profile
    serializer = ProfileSerializer(profile, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)