from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from .models import Tournament
from .serializers import TournamentListSerializers


class TournamentView(viewsets.ViewSet):

    def list(self, request):
        queryset = Tournament.objects.all()
        serializer = TournamentListSerializers(
            queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
