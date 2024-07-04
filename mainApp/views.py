from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Qoshiqchi, Albom, Qoshiq
from .serializers import QoshiqchiSerializer, AlbomSerializer, QoshiqSerializer

# Qoshiqchi Views
class QoshiqchiListCreateAPIView(ListCreateAPIView):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer
    # permission_classes = [IsAuthenticated]

class QoshiqchiRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer
    # permission_classes = [IsAuthenticated]

# Albom Views
class AlbomListCreateAPIView(ListCreateAPIView):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    # permission_classes = [IsAuthenticated]

class AlbomRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    # permission_classes = [IsAuthenticated]

# Qoshiq Views
class QoshiqListCreateAPIView(ListCreateAPIView):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer
    # permission_classes = [IsAuthenticated]

class QoshiqRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer
    # permission_classes = [IsAuthenticated]
