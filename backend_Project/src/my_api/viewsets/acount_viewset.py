from rest_framework.viewsets import ModelViewSet
from my_api.models import Acount
from my_api.serializers import AcountSerializer

class AcountViewSet(ModelViewSet):
    queryset = Acount.objects.all()
    serializer_class = AcountSerializer
    filter_fields = {
        'id': ['exact'],
    }
