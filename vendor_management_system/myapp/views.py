from rest_framework import generics, status
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Avg, F
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer

class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save()

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        self.update_vendor_performance(instance.vendor)

    def update_vendor_performance(self, vendor):
        completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        total_completed_pos = completed_pos.count()

        if total_completed_pos > 0:
            on_time_deliveries = completed_pos.filter(delivery_date__lte=timezone.now())
            on_time_delivery_rate = (on_time_deliveries.count() / total_completed_pos) * 100

            quality_rating_avg = completed_pos.aggregate(Avg('quality_rating'))['quality_rating__avg']

            avg_response_time = completed_pos.aggregate(Avg(F('acknowledgment_date') - F('issue_date')))['acknowledgment_date__avg']

            fulfilled_pos = completed_pos.exclude(quality_rating__isnull=True)
            fulfillment_rate = (fulfilled_pos.count() / total_completed_pos) * 100

            vendor.on_time_delivery_rate = on_time_delivery_rate
            vendor.quality_rating_avg = quality_rating_avg
            vendor.average_response_time = avg_response_time.total_seconds() if avg_response_time else 0
            vendor.fulfillment_rate = fulfillment_rate
            vendor.save()

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        self.update_vendor_performance(instance.vendor)

    def perform_destroy(self, instance):
        self.update_vendor_performance(instance.vendor)
        instance.delete()

    def update_vendor_performance(self, vendor):
        completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        total_completed_pos = completed_pos.count()

        if total_completed_pos > 0:
            on_time_deliveries = completed_pos.filter(delivery_date__lte=timezone.now())
            on_time_delivery_rate = (on_time_deliveries.count() / total_completed_pos) * 100

            quality_rating_avg = completed_pos.aggregate(Avg('quality_rating'))['quality_rating__avg']

            avg_response_time = completed_pos.aggregate(Avg(F('acknowledgment_date') - F('issue_date')))['acknowledgment_date__avg']

            fulfilled_pos = completed_pos.exclude(quality_rating__isnull=True)
            fulfillment_rate = (fulfilled_pos.count() / total_completed_pos) * 100

            vendor.on_time_delivery_rate = on_time_delivery_rate
            vendor.quality_rating_avg = quality_rating_avg
            vendor.average_response_time = avg_response_time.total_seconds() if avg_response_time else 0
            vendor.fulfillment_rate = fulfillment_rate
            vendor.save()

class VendorPerformanceAPIView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        vendor = self.get_object()
        performance_data = {
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'average_response_time': vendor.average_response_time,
            'fulfillment_rate': vendor.fulfillment_rate
        }
        return Response(performance_data, status=status.HTTP_200_OK)
