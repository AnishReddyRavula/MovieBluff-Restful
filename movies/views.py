from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from movies.models import Movies
from moviebluff.serializers import MovieDataSerializer



class CreateView(generics.ListCreateAPIView):
	"""This class defines the create behavior of our rest api."""
	queryset = Movies.objects.all()
	serializer_class = MovieDataSerializer

	def perform_create(self, serializer):
		"""Save the post data when creating a new movie data."""
		serializer.save()

# Create your views here.
# @api_view(['GET', 'POST'])
# def movie_list(request):
# 	if request.method == 'GET':
# 		movies_list = Movies.objects.all()
# 		serializer = MovieDataSerializer(movies_list, many=True)
# 		return Response(serializer.data)

# 	elif request.method == 'POST':
# 		serializer = MovieDataSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		else:
# 			return Response(
# 				serializer.errors,
# 				status=status.HTTP_400_BAD_REQUEST
# 			)
	

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     """
#     Get, udpate, or delete a specific task
#     """
#     try:
#         movie_objects = Movies.objects.get(pk=pk)
#     except Movies.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = MovieDataSerializer(movie_objects)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = MovieDataSerializer(movie_objects, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(
#                 serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         movie_objects.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)