from rest_framework import serializers

from .models import Card, Board, Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id', 
            'name',
            'description',
            'is_marked',
            'get_absolute_url',
            'status'
        )

class BoardSerializer(serializers.HyperlinkedModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Board
        fields = (
            'id',
            'name',
            'description',
            'get_absolute_url',
            'tasks'
        )

class CardSerializer(serializers.HyperlinkedModelSerializer):
    boards = BoardSerializer(many=True)

    class Meta:
        model = Card
        fields = (
            'id',
            'name',
            'description',
            'image',
            'is_marked',
            'is_visible',
            'is_history',
            'get_absolute_url',
            'boards'
        )