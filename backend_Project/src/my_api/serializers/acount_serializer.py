from rest_framework import serializers
from my_api.models import Acount


class AcountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acount
        exclude = [
            "created_at",
            "updated_at",
        ]
