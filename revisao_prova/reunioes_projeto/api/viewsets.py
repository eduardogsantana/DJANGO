from rest_framework import viewsets
from reunioes_projeto.models import Reuniao
from .serializers import ReuniaoSerializer

class ReuniaoViewSet(viewsets.ModelViewSet):
    queryset = Reuniao.objects.all()
    serializer_class = ReuniaoSerializer