from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Card, Board, Task
from .serializers import CardSerializer, BoardSerializer, TaskSerializer

import json
from collections import OrderedDict

class CardsView(APIView):
    def get(self, request, format=None):
        cards = Card.objects.filter(Q(user=request.user))
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        cards = Card.objects.filter(user=request.user)
        cards.create(
            user=request.user,
            name=request.data['name'],
            description=request.data['description'],
            image=request.data['image'],
            is_marked=request.data['is_marked'],
            is_visible=request.data['is_visible'],
            slug=request.data['slug']
        )
        return Response({"Cards": []})

    def delete(self, request, format=None):
        cards = Card.objects.filter(user=request.user)
        cards.filter(
            id=request.data['target_card_id']
        ).delete()
        return Response({"Cards": []})

    def put(self, request, format=None):
        print(request.data)
        cards = Card.objects.filter(user=request.user)
        target_card = cards.get(
            id=request.data['target_card_id']
        )
        target_card.name = request.data['name']
        target_card.description = request.data['description']
        target_card.image = request.data['image']
        target_card.is_marked = request.data['is_marked']
        target_card.is_visible = request.data['is_visible']
        target_card.is_history = request.data['is_history']
        target_card.slug = request.data['slug']
        target_card.save()
        return Response({"Cards": []})

class BoardsView(APIView):
    def get(self, request, format=None):
        boards = Board.objects.filter(user=request.user)
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        boards = Board.objects.filter(user=request.user)

        target_card = Card.objects.filter(Q(user=request.user) & Q(id=request.data['target_card_id']))
        boards.create(
            user=request.user,
            card=target_card[0], 
            name=request.data['name'],
            description=request.data['description'],
            slug=request.data['slug']
        )
        return Response({"Boards": []})

    def delete(self, request, format=None):
        boards = Board.objects.filter(user=request.user)

        target_card = Card.objects.filter(Q(user=request.user) & Q(id=request.data['target_card_id']))

        boards.filter(
            user=request.user,
            card=target_card[0],
            id=request.data['id']
        ).delete()
        return Response({"Boards": []})
    
    def put(self, request, format=None):
        boards = Board.objects.filter(user=request.user)
            
        target_board = boards.get(
            id=request.data['target_board_id']
        )
        target_board.card = Card.objects.get(Q(user=request.user) & Q(id=request.data['target_card_id']))
        target_board.name = request.data['name']
        target_board.description = request.data['description']
        target_board.slug = request.data['slug']
        target_board.save()
        return Response({"Boards": []})

class TasksView(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        tasks = Task.objects.filter(user=request.user)

        target_board = Board.objects.filter(Q(user=request.user) & Q(id=request.data['target_board_id']))
        tasks.create(
            user=request.user,
            board=target_board[0], 
            name=request.data['name'],
            description=request.data['description'],
            is_marked=request.data['is_marked'],
            status=request.data['status'],
            slug=request.data['slug']
        )
        return Response({"Tasks": []})

    def delete(self, request, format=None):
        tasks = Task.objects.filter(user=request.user)

        target_board = Board.objects.filter(Q(user=request.user) & Q(id=request.data['target_board_id']))

        print(target_board[0])
        print(tasks[0].board)
        tasks.filter(
            user=request.user,
            board=target_board[0],
            id=request.data['id']
        ).delete()
        return Response({"Tasks": []})
    
    def put(self, request, format=None):
        tasks = Task.objects.filter(user=request.user)

        target_task = tasks.get(
            id=request.data['target_task_id']
        )
        target_task.board = Board.objects.get(Q(id=request.data['target_board_id']))
        target_task.name = request.data['name']
        target_task.description = request.data['description']
        target_task.is_marked = request.data['is_marked']
        target_task.status = request.data['status']
        target_task.slug = request.data['slug']
        target_task.save()
        return Response({"Tasks": []})

class TaskDetail(APIView):
    def get_object(self, request, card_slug, board_slug, task_slug):
        try:
            return Task.objects.filter(user=request.user).filter(card__slug=card_slug).filter(board__slug=board_slug).get(slug=task_slug)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, card_slug, board_slug, task_slug, format=None):
        task = self.get_object(request, card_slug, board_slug, task_slug)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

class BoardDetail(APIView):
    def get_object(self, request, card_slug, board_slug):
        try:
            return Board.objects.filter(user=request.user).filter(card__slug=card_slug).get(slug=board_slug)
        except Board.DoesNotExist:
            raise Http404

    def get(self, request, card_slug, board_slug, format=None):
        board = self.get_object(request, card_slug, board_slug)
        serializer = BoardSerializer(board)
        return Response(serializer.data)

class CardDetail(APIView):
    def get_object(self, request, card_slug):
        try:
            return Card.objects.filter(user=request.user).get(slug=card_slug)
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, card_slug, format=None):
        card = self.get_object(request, card_slug)
        serializer = CardSerializer(card)
        return Response(serializer.data)

@api_view(['POST'])
def card_search(request):
    query = request.data.get('query', '')

    if query:
        cards = Card.objects.filter(Q(user=request.user) & (Q(name__icontains=query) | Q(description__icontains=query)))
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)
    else:
        return Response({"Cards": []})

@api_view(['POST'])
def board_search(request):
    query = request.data.get('query', '')

    if query:
        boards = Board.objects.filter(Q(user=request.user) & (Q(name__icontains=query) | Q(description__icontains=query)))
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)
    else:
        return Response({"Boards": []})

@api_view(['POST'])
def task_search(request):
    query = request.data.get('query', '')

    if query:
        tasks = Task.objects.filter(Q(user=request.user) & (Q(name__icontains=query) | Q(description__icontains=query)))
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    else:
        return Response({"Tasks": []})