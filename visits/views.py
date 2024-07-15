from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Worker, RetailPoint, Visit
from .serializers import RetailPointSerializer, VisitSerializer
from .authentication import PhoneNumberAuthentication
from rest_framework.permissions import IsAuthenticated

class RetailPointList(APIView):
    authentication_classes = [PhoneNumberAuthentication]

    def get(self, request):
        worker = request.user
        retail_points = RetailPoint.objects.filter(worker=worker)
        if not retail_points:
            return Response({"error": "No retail points found for this worker."}, status=status.HTTP_404_NOT_FOUND)
        serializer = RetailPointSerializer(retail_points, many=True)
        return Response(serializer.data)

class VisitCreate(APIView):
    authentication_classes = [PhoneNumberAuthentication]

    def post(self, request):
        worker = request.user
        retail_point_id = request.data.get('retail_point_id')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        print(worker)
        try:
            retail_point = RetailPoint.objects.get(id=retail_point_id, worker_id=worker.id)
            print(retail_point)
            visit = Visit.objects.create(retail_point=retail_point, worker=worker, latitude=latitude, longitude=longitude)
            serializer = VisitSerializer(visit)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except RetailPoint.DoesNotExist as e:
            print(e)
            return Response({"error": "Invalid retail point for this worker."}, status=status.HTTP_400_BAD_REQUEST)