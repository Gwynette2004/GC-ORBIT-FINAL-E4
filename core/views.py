from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny  # 🔥 Add this line
from rest_framework.permissions import IsAuthenticated


class CustomUserLoginView(APIView):
    permission_classes = [AllowAny]  # 🔥 Add this line

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            
            return Response({
                "access": str(access_token),
                "refresh": str(refresh)
            }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]  # 🔥 Add this line

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"detail": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProtectedHelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello {request.user.email}, you are authenticated!"})