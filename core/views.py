from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers import UserSerializer  # Import the UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import User

class UserSignupView(APIView):
    permission_classes = []  # Allow all users to access this endpoint

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
        if user.status == User.NEW_CUSTOMER and new_status == User.INSURED_CUSTOMER:
            user.status = User.INSURED_CUSTOMER
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

