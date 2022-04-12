from rest_framework import generics
from .models import Qcms, Question
from .serializers import QcmSerializer
from rest_framework.views import APIView

class Qcm(generics.ListAPIView):
    
    serializer_class = QcmSerializer
    queryset = Qcms.objects.all()
    
class RandomQuestion(APIView):
    
    def get(self, request, format:None, **kwargs):
        question = Question.objects.filter()