from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from .models import Tournament
from .serializers import TournamentListSerializers, TeamPerTournSerializers


class TournamentView(viewsets.ModelViewSet):

    serializer_class = TournamentListSerializers
    queryset = Tournament.objects.all()
    lookup_field = 'name'

    def list(self, request):
        queryset = Tournament.objects.all()
        serializer = TournamentListSerializers(
            queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        queryset = Tournament.objects.get(pk=pk).tourn_team.all()
        serializer = TeamPerTournSerializers(
            queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
