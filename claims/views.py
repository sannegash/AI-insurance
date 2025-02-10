from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Claim
from .serializers import ClaimSerializer
from vehicle.models import Vehicle
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['POST'])
def create_claim(request):
    """
    Create a new claim.
    """
    serializer = ClaimSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Saves the claim to the database
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_claims(request):
    """
    List all claims.
    """
    claims = Claim.objects.all()
    serializer = ClaimSerializer(claims, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
def update_claim(request, pk):
    """
    Get or update a specific claim.
    """
    try:
        claim = Claim.objects.get(pk=pk)
    except Claim.DoesNotExist:
        return Response({"detail": "Claim not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClaimSerializer(claim)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClaimSerializer(claim, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
