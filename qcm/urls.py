from django.urls import path
from .views import Qcm

app_name = 'qcm'

urlpatterns = [
    path('', Qcm.as_view(), name='qcm'),
]
