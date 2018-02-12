from rest_framework import generics #This module helps us to handle get, post, dlete, put requests
from movies.models import Movies #Movies model
from moviebluff.serializers import MovieDataSerializer #Serializer to map the Model instance into JSON format

class CreateView(generics.ListCreateAPIView):
	""" This class defines the create behavior of our rest api."""
	queryset = Movies.objects.all()
	serializer_class = MovieDataSerializer

	def perform_create(self, serializer):
		"""Save the post data when creating a new movie data."""
		serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	""" This class handles the http GET, PUT and DELETE requests."""

	queryset = Movies.objects.all()
	serializer_class = MovieDataSerializer
