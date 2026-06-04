from rest_framework.viewsets import ModelViewSet
from .models import Perfume
from .serializers import PerfumeSerializer

class PerfumeViewSet(ModelViewSet):
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer