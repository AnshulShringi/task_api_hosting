from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from api.models import IrisDataset
from api.serializers import IrisDatasetSerializer


# Create your views here.
class IrisListCreateView(LoginRequiredMixin, generics.ListCreateAPIView):
    login_url = '/accounts/login/'
    # redirect_field_name = '/accounts/google/login/callback/'
    queryset = IrisDataset.objects.all()
    serializer_class = IrisDatasetSerializer