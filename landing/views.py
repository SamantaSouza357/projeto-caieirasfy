from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from landing.models import Musica
from landing.serializers import MusicaSerializer


# Create your views here.


class MusicaViewset(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nomeMusica', '^artista', '^genero', '^link']
    queryset = Musica.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = MusicaSerializer
