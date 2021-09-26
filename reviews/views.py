from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import YelpBusinessItem
from .serializers import YelpBusinessItemSerializer


class YelpBusinessItemViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = YelpBusinessItem.objects.all()
    serializer_class = YelpBusinessItemSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(created_by=self.request.user)
        return query_set
