from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
from core.serializers import UserSerializer  # Import the UserSerializer
from .models import User


class UserSignupView(APIView):
    permission_classes = [AllowAny]  # Allow all users to access this endpoint

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)  # Use UserSerializer here
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_user_status(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        # Ensure the user is an Underwriter
        if request.user.role != User.UNDERWRITER:
            raise PermissionDenied("You do not have permission to perform this action.")
        
        new_status = request.data.get('status')
        
        # Ensure that the status is valid
        if new_status not in [User.NEW_CUSTOMER, User.INSURED_CUSTOMER]:
            return Response({'error': 'Invalid status'}, status=400)

        # Check if the user is in 'NEW_CUSTOMER' status and update to 'INSURED_CUSTOMER'
        if user.role == User.NEW_CUSTOMER and new_status == User.INSURED_CUSTOMER:
            user.role = User.INSURED_CUSTOMER
            user.save()

            # Serialize the updated user data to return
            updated_user_serializer = UserSerializer(user)
            return Response({
                'message': 'User status updated to Insured Customer',
                'user': updated_user_serializer.data
            })

        return Response({'error': 'Invalid status transition'}, status=400)

    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

class SignInView(APIView):
    """
    Handles user login by authenticating the user with username and password.
    Returns JWT tokens (access and refresh) and user information upon successful login.
    """
    permission_classes = []
    def post(self, request, *args, **kwargs):
        # Extract username and password from request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Check if both username and password are provided
        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Create JWT tokens (access and refresh)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)  # Access token
            refresh_token = str(refresh)  # Refresh token

            # Ensure the 'role' field exists on your custom User model
            user_data = {
                "username": user.username,
                "role": user.role,  # Ensure 'role' is correctly set in your custom user model
            }

            # Return the tokens and user details
            return Response({
                "message": "Sign-in successful",
                "access": access_token,
                "refresh": refresh_token,
                "user": user_data  # Now this will include the 'role'
            }, status=status.HTTP_200_OK)

        # If authentication fails, return an error
        return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)