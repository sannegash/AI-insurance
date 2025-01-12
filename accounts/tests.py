from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User, Group
from app_name.models import NewCustomer

class VerifyNewCustomerTest(APITestCase):
    
    def setUp(self):
        # Create an underwriter group
        self.underwriter_group = Group.objects.create(name='Underwriter')
        
        # Create users
        self.underwriter = User.objects.create_user(username='underwriter', password='password')
        self.underwriter.groups.add(self.underwriter_group)
        
        self.non_underwriter = User.objects.create_user(username='non_underwriter', password='password')
        
        # Create a new customer
        self.new_customer = NewCustomer.objects.create(
            name='John Doe',
            status='Pending'
        )
        
        # Set the URL for the PATCH request
        self.url = f'/api/verify_customer/{self.new_customer.id}/'

    def test_verify_new_customer_as_underwriter(self):
        """Test that an underwriter can verify a new customer and convert to insured."""
        # Authenticate as underwriter
        self.client.login(username='underwriter', password='password')
        
        response = self.client.patch(self.url)
        self.new_customer.refresh_from_db()  # Reload the customer object from DB
        
        # Check that the status is updated to "Insured"
        self.assertEqual(self.new_customer.status, 'Insured')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Customer successfully verified and converted to Insured.')

    def test_verify_new_customer_as_non_underwriter(self):
        """Test that a non-underwriter cannot verify a customer."""
        # Authenticate as a non-underwriter
        self.client.login(username='non_underwriter', password='password')
        
        response = self.client.patch(self.url)
        
        # Check that the status is not updated
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'], 'You do not have permission to verify customers.')

    def test_verify_new_customer_already_verified(self):
        """Test that a customer with status 'Insured' cannot be verified again."""
        # Change the status of the customer to Insured
        self.new_customer.status = 'Insured'
        self.new_customer.save()
        
        # Authenticate as underwriter
        self.client.login(username='underwriter', password='password')
        
        response = self.client.patch(self.url)
        
        # Check for a 400 Bad Request response because the customer is already verified
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'This customer is already verified or rejected.')

    def test_verify_new_customer_not_found(self):
        """Test that if the customer does not exist, a 404 is returned."""
        # Authenticate as underwriter
        self.client.login(username='underwriter', password='password')
        
        invalid_url = '/api/verify_customer/9999/'  # Non-existing customer ID
        response = self.client.patch(invalid_url)
        
        # Check that a 404 Not Found is returned
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'Customer not found')
