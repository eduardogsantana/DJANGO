from rest_framework import viewsets
from cad_unico.models import Beneficiarios
from .serializers import BeneficiariosSerializer

class BeneficiariosViewSet(viewsets.ModelViewSet):
    queryset = Beneficiarios.objects.all()
    serializer_class = BeneficiariosSerializer