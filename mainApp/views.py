from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet


# class QoshiqchilarAPIView(APIView):
#     def get(self, request):
#         qoshiqchilar = Qoshiqchi.objects.all()
#         serializer = QoshiqchiSerializer(
#             qoshiqchilar, many=True
#         )
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = QoshiqchiSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
#
# class QoshiqchiTahrirlashAPIView(APIView):
#     def put(self, request, pk):
#         qoshiqchi = get_object_or_404(Qoshiqchi, pk=pk)
#         serializer = QoshiqchiSerializer(qoshiqchi, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#
#
# class QoshiqchiDeleteAPIView(APIView):
#     def delete(self, request, pk):
#         qoshiqchi = get_object_or_404(Qoshiqchi, id=pk)
#         qoshiqchi.delete()
#         return Response('Qoshiqchi ochirildi')

# class QoshiqlarAPIView(APIView):
#     def get(self, request):
#         qoshiqlar = Qoshiq.objects.all()
#         serializer = QoshiqSerializer(
#             qoshiqlar, many=True
#         )
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = QoshiqSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

class QoshiqModelViewSet(ModelViewSet):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer

    search_fields = ['nom', 'janr' ]
    ordering_fields = ['davomiylik', ]

class AlbomlarModelViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer

    search_fields = ['nom', ]
    ordering_fields = ['sana', ]

    @action(detail=True, methods=['get'])
    def qoshiqlar(self, request, pk):
        albom = self.get_object()
        qoshiqlar = Qoshiq.objects.filter(albom=albom)
        serializer = QoshiqSerializer(qoshiqlar, many=True)
        return Response(serializer.data)

class QoshiqchilarModelViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ['ism', 'davlat']
    ordering_fields = ['t_yil', ]

    @action(detail=True, methods=['get'])
    def albomlar(self, request, pk):
        qoshiqchi = self.get_object()
        albomlar = Albom.objects.filter(qoshiqchi=qoshiqchi)
        serializer = AlbomSerializer(albomlar, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def qosh_albom(self, request, pk=None):
        qoshiqchi = self.get_object()
        serializer = AlbomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(qoshiqchi=qoshiqchi)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


