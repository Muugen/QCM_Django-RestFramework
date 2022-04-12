from rest_framework import serializers
from .models import Qcms


class QcmSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Qcms
        fields = [ 
            'title',
        ]