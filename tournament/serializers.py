from .models import Tournament, Teams
from rest_framework import serializers


class TournamentListSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tournament
        fields = ('id', 'name', 'photo_img')


class TeamPerTournSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Teams
        fields = ('id', 'name', 'photo_img')
