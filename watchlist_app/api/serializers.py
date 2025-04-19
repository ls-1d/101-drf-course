from rest_framework import serializers
from watchlist_app.models import Watchlist, StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):

    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
