from rest_framework import serializers
from applications.feedback.models import Like, Rating

class LikeSerialier(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class RetingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value = 5)
    class Meta:
        model = Rating
        fields = ('rating',)