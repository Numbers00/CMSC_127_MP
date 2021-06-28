from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.views.decorators.csrf import csrf_exempt


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
