
# serializers.py
from rest_framework import serializers
from .models import Vendor, PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '_all_'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '_all_'
