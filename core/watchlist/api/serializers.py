from rest_framework import serializers
from core.watchlist.models import Movie, StreamingPlatform


def title_length(value):
    if len(value) < 2:
        raise serializers.ValidationError(f"{value} is too short")


class MovieSeriazer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    plot = serializers.CharField(validators=[title_length])
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.title = validated_data.get("title", instance.title)
        instance.plot = validated_data.get("plot", instance.plot)
        instance.active = validated_data.get("active", instance.active)
        instance.created_at = validated_data.get("created", instance.created_at)
        instance.updated = validated_data.get("created", instance.created_at)
        instance.save()
        return instance

    def validate_title(self, value):
        """
        Field Level Validation
        Check if movie title is less than 2.
        """
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        return value

    def validate(self, data):
        """
        Object Level Validation
        Title and description should not be the same
        """
        if data["title"].capitalizer() == data["plot"].capitalize():
            raise serializers.ValidationError("Title and description should be different.")
        return data


class MovieModelSerializer(serializers.ModelSerializer):
    len_title = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "plot", "active", "platform", "len_title", "created_at", "updated_at"]

    def validate_title(self, value):
        """
        Field Level Validation
        Check if movie name is less than 2.
        """
        if len(value) < 2:
            raise serializers.ValidationError("Title is too short")
        return value

    def validate(self, data):
        """
        Object Level Validation
        Title and description should not be the same
        """
        if data["title"].capitalize() == data["plot"].capitalize():
            raise serializers.ValidationError("Title and plot should be different.")
        return data

    def get_len_title(self, obj):
        """
        Serializer method field
        """
        return len(obj.title)


class StreamingPlatformMS(serializers.ModelSerializer):
    movies = MovieModelSerializer(many=True, read_only=True)
    class Meta:
        model = StreamingPlatform
        fields = ["name", "about", "website", "movies"]
