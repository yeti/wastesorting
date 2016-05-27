from rest_framework import serializers

from whatbin.models import Bin, Item

class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = ('id', 'title', 'description')


class ItemSerializer(serializers.ModelSerializer):
    bin = BinSerializer()

    class Meta:
        model = Item
        fields = ('id', 'title', 'bin')