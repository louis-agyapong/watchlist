from rest_framework import serializers
from core.watchlist.models import Movie


class MovieSeriazer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.active = validated_data.get("active", instance.active)
        instance.save()
        return instance

    def validate_name(self, value):
        """
        Field Level Validation
        Check if movie name is less than 2.
        """
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        return value