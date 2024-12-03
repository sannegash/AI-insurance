from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomerSignupSerializer


class StaffSignView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = StaffSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message'; 'Signup successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerSignupView(generics.CreateAPTView):
    serializer_class = CustomerSignupSerializer