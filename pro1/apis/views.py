from rest_framework import viewsets

from .serializer import empSerializer

from .models import emp

class empViewSet(viewsets.ModelViewSet):
    queryset=emp.objects.all()
    serializer_class=empSerializer
    