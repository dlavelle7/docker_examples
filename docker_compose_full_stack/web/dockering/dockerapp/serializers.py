from rest_framework import serializers

from .models import Foo


class FooSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=60)
    created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Foo
        fields = ('id', 'title', 'created')
