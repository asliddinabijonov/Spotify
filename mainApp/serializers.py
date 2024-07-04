from rest_framework import serializers
from .models import Qoshiqchi, Albom, Qoshiq


class QoshiqchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiqchi
        fields = ['id', 'ism', 't_yil', 'davlat']


class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = ['id', 'nom', 'sana', 'rasm', 'qoshiqchi']

        extra_kwargs = {
            'rasm': {'required': False}
        }


class QoshiqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qoshiq
        fields = ['id', 'nom', 'janr', 'davomiylik', 'fayl', 'albom']

    def validate_fayl(self, value):
        if not str(value).endswith('.mp3'):
            raise serializers.ValidationError('bunday kengaymani qabul qilmaydi')
        return value

    def validate_davomiylik(self, value):
        davomiylik = str(value).split(":")
        if int(davomiylik[-2]) >= 7 | int(davomiylik[-3]) <= 0:
            raise serializers.ValidationError('7 daqiqadan oshmasligi kerak')
        return value
