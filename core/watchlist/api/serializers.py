# from rest_framework import serializers
# from core.watchlist.models import Movie


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError(f"{value} is too short")


# class MovieSeriazer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[name_length])
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.id = validated_data.get("id", instance.id)
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance

#     def validate_name(self, value):
#         """
#         Field Level Validation
#         Check if movie name is less than 2.
#         """
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#         return value

#     def validate(self, data):
#         """
#         Object Level Validation
#         Title and description should not be the same
#         """
#         if data["name"].capitalizer() == data["description"].capitalize():
#             raise serializers.ValidationError("Title and description should be different.")
#         return data


# class MovieModelSerializer(serializers.ModelSerializer):
#     len_name = serializers.SerializerMethodField()

#     class Meta:
#         model = Movie
#         fields = ["id", "name", "description", "active", "len_name"]

#     def validate_name(self, value):
#         """
#         Field Level Validation
#         Check if movie name is less than 2.
#         """
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#         return value

#     def validate(self, data):
#         """
#         Object Level Validation
#         Title and description should not be the same
#         """
#         if data["name"].capitalize() == data["description"].capitalize():
#             raise serializers.ValidationError("Title and description should be different.")
#         return data

#     def get_len_name(self, obj):
#         return len(obj.name)
