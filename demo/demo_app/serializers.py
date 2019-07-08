from rest_framework import serializers

from .models import biomodel
class BioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = biomodel
        fields = '__all__'
