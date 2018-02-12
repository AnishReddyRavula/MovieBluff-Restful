from rest_framework import serializers

from movies.models import Movies

class MovieDataSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Movies
        fields = ('movie_name', 'movie_rating', 'watched')
        read_only_fields = (['id'])