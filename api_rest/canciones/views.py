from rest_framework import viewsets
from .serializers import CancionSerializer
from .models import Cancion

class CancionView(viewsets.ModelViewSet):
    serializer_class = CancionSerializer
    queryset = Cancion.objects.all()


