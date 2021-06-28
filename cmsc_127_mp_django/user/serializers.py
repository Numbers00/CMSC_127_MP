from rest_framework import serializers

from task.serializers import TaskSerializer, BoardSerializer, CardSerializer

from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):   
    tasks = TaskSerializer(many=True)
    boards = BoardSerializer(many=True)
    cards = CardSerializer(many=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "bio",
            "quote",
            "profile_picture",
            "bg_image",
            "plan_level",
            "password",
            "is_visible",
            "get_absolute_url",
            "tasks",
            "boards",
            "cards"
        )