from DjangoCustomUser.api import serializers

from testp import api


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = api
        fields = ('id', 'email', 'password')
