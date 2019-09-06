from rest_framework import serializers
from landing.models import Musica


# fields =(__all__) para pegar todos os atributos da model no django-rest
class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = ('id','nomeMusica','artista','genero','link')