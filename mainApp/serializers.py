from rest_framework import serializers
from .models import *

class QoshiqchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = '__all__'

class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = '__all__'

class QoshiqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = '__all__'

    def validate_fayl(self, value):
        if not str(value).endswith('.mp3'):
            raise serializers.ValidationError('bunday kengaymani qabul qilmaydi')
        return value
    def validate_davomiylik(self, value):
        davomiylik = str(value).split(":")
        if int(davomiylik[-2]) >= 7 | int(davomiylik[-3]) <=0:
            raise serializers.ValidationError('7 daqiqadan oshmasligi kerak')
        return value