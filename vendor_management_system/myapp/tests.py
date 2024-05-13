from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer

class VendorAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor1 = Vendor.objects.create(name='Vendor 1')
        self.vendor2 = Vendor.objects.create(name='Vendor 2')
        self.purchase_order1 = PurchaseOrder.objects.create(vendor=self.vendor1)
        self.purchase_order2 = PurchaseOrder.objects.create(vendor=self.vendor2)

    def test_vendor_list(self):
        response = self.client.get(reverse('vendor-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)# Assuming 2 vendors created in setUp

    def test_vendor_detail(self):
        response = self.client.get(reverse('vendor-detail', args=[self.vendor1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Vendor 1')
        # Add more assertions as needed

    def test_create_vendor(self):
        data = {'name': 'New Vendor'}  # Add necessary data for creating a vendor
        response = self.client.post(reverse('vendor-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 3)  # Assuming 2 vendors were created in setUp

    def test_update_vendor(self):
        data = {'name': 'Updated Vendor'}  # Add necessary data for updating a vendor
        response = self.client.put(reverse('vendor-detail', args=[self.vendor1.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vendor1.refresh_from_db()
        self.assertEqual(self.vendor1.name, 'Updated Vendor')
        # Add more assertions as needed
    def setUp(self):
        self.client = APIClient()
        self.vendor1 = Vendor.objects.create(name='Vendor 1')
        self.vendor2 = Vendor.objects.create(name='Vendor 2')
        self.purchase_order1 = PurchaseOrder.objects.create(vendor=self.vendor1)
        self.purchase_order2 = PurchaseOrder.objects.create(vendor=self.vendor2)

    def test_vendor_list(self):
        response = self.client.get(reverse('vendor-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Assuming 2


   
