from .models import Tournament
from rest_framework import serializers
from django.contrib.sites.shortcuts import get_current_site


class TournamentListSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tournament
        fields = ('id', 'name', 'photo_img')
