from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from .models import Tournament
from .serializers import TournamentListSerializers


class TournamentView(viewsets.ModelViewSet):

    serializer_class = TournamentListSerializers
    queryset = Tournament.objects.all()

    def list(self, request):
        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
