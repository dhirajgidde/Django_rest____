from rest_framework import serializers
from .models import Tuterials


class TuterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tuterials
        fields = ('id', 'title', 'description', 'published')
