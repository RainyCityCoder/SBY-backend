from rest_framework import serializers
from .models import Biologists, ComputerScientists

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biologists
        fields = ["id", "name", "birthyear"]
        
        
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerScientists
        fields = ["id", "name", "birthyear"]