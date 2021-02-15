from rest_framework import serializers
from Lounge.models import AirpotLoungeModel

class LoungeSerializer(serializers.ModelSerializer):

    class Meta():
        model = AirpotLoungeModel
        fields = '__all__'

