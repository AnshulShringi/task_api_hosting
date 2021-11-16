from rest_framework import serializers
from .models import IrisDataset


class IrisDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrisDataset
        fields = "__all__"