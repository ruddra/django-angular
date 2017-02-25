from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing movie instances.
    """
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
