from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Card, Board, Task
from .serializers import CardSerializer, BoardSerializer, TaskSerializer

class CardsView(APIView):
    def get(self, request, format=None):
        cards = Card.objects.filter(user=request.user)
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
            name=request.data['target_card_name']
        ).delete()
        return Response({"Cards": []})

    def put(self, request, format=None):
        cards = Card.objects.filter(user=request.user)
        target_card = cards.get(
            name=request.data['target_card_name']
        )
        target_card.first_name = request.data['name']
        target_card.description = request.data['description']
        target_card.image = request.data['image']
        target_card.is_marked=request.data['is_marked'],
        target_card.is_visible = request.data['is_visible']
        target_card.slug = request.data['slug']
        target_card.save()
        return Response({"Cards": []})

class BoardsView(APIView):
    def get(self, request, format=None):

        cards = Card.objects.filter(user=request.user)
        serializer = CardSerializer(cards, many=True)
        boards = []
        for data in serializer.data:
            boards.append(data['boards'])
        return Response(boards)

    def post(self, request, format=None):
        cards = Card.objects.filter(user=request.user)
        serializer = CardSerializer(cards, many=True)
        boards = []
        for data in serializer.data:
            boards.append(data['boards'])

        target_card = Card.objects.filter(Q(user=request.user) & Q(name=request.data['target_card_name']))
        boards.create(
            card=target_card[0], 
            name=request.data['name'],
            description=request.data['description'],
            slug=request.data['slug']
        )
        return Response({"Boards": []})

    def delete(self, request, format=None):
        cards = Card.objects.filter(user=request.user)
        serializer = CardSerializer(cards, many=True)
        boards = []
        for data in serializer.data:
            boards.append(data['boards'])

        boards.filter(
            name=request.data['name']
        ).delete()
        return Response({"Boards": []})
    
    def put(self, request, format=None):
        cards = Card.objects.filter(user=request.user)
        serializer = CardSerializer(cards, many=True)
        boards = []
        for data in serializer.data:
            boards.append(data['boards'])
            
        target_board = boards.get(
            name=request.data['name']
        )
        target_board.card = Card.objects.get(Q(user=request.user) & Q(name=request.data['target_card_name']))
        target_board.name = request.data['name']
        target_board.description = request.data['description']
        target_board.slug = request.data['slug']
        target_board.save()
        return Response({"Lists": []})

class TasksView(APIView):
    def get(self, request, format=None):
        cards = Card.objects.filter(user=request.user)
        card_serializer = CardSerializer(cards, many=True)
        tasks = []
        for data in card_serializer.data:
            for board in data['boards']:
                tasks.append(board['tasks'])
        return Response(tasks)

    def post(self, request, format=None):
        cards = Card.objects.filter(user=request.user)
        card_serializer = CardSerializer(cards, many=True)
        tasks = []
        for data in card_serializer.data:
            for board in data['boards']:
                tasks.append(board['tasks'])

        target_board = Board.objects.filter(Q(user=request.user) & Q(name=request.data['target_board_name']))
        tasks.create(
            board=target_board[0],
            name=request.data['name'],
            description=request.data['description'],
            is_marked=request.data['is_marked'],
            status=request.data['status'],
            slug=request.data['slug']
        )
        return Response({"Tasks": []})

    def delete(self, request, format=None):
        cards = Card.objects.filter(user=request.user)
        card_serializer = CardSerializer(cards, many=True)
        tasks = []
        for data in card_serializer.data:
            for board in data['boards']:
                tasks.append(board['tasks'])

        tasks.filter(
            board=Board.objects.filter(Q(user=request.user) & Q(name=request.data['target_board_name']))[0],
            name=request.data['name']
        ).delete()
        return Response({"Tasks": []})
    
    def put(self, request, format=None):
        cards = Card.objects.filter(user=request.user)
        card_serializer = CardSerializer(cards, many=True)
        tasks = []
        for data in card_serializer.data:
            for board in data['boards']:
                tasks.append(board['tasks'])

        target_task = tasks.get(
            name=request.data['name']
        )
        target_task.board = Board.objects.get(Q(user=request.user) & Q(name=request.data['target_board_name']))
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
            cards = Card.objects.filter(user=request.user)
            card_serializer = CardSerializer(cards, many=True)
            tasks = []
            for data in card_serializer.data:
                for board in data['boards']:
                    tasks.append(board['tasks'])
            return tasks.filter(card__slug=card_slug).filter(board__slug=board_slug).get(slug=task_slug)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, card_slug, board_slug, task_slug, format=None):
        task = self.get_object(request, card_slug, board_slug, task_slug)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

class BoardDetail(APIView):
    def get_object(self, request, card_slug, board_slug):
        try:
            cards = Card.objects.filter(user=request.user)
            serializer = CardSerializer(cards, many=True)
            boards = []
            for data in serializer.data:
                boards.append(data['boards'])
            return boards.filter(card__slug=card_slug).get(slug=board_slug)
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
        cards = Card.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)
    else:
        return Response({"Cards": []})

@api_view(['POST'])
def board_search(request):
    query = request.data.get('query', '')

    if query:
        boards = Board.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)
    else:
        return Response({"Boards": []})

@api_view(['POST'])
def task_search(request):
    query = request.data.get('query', '')

    if query:
        tasks = Task.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    else:
        return Response({"Tasks": []})