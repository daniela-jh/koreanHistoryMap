from rest_framework import viewsets
from .serializers import ContentSerializer
from .models import Content

class ContentView(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    # permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()
