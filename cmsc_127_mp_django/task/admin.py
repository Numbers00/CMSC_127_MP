from django.contrib import admin

from .models import Card, Board, Task

# Register your models here.
admin.site.register(Card)
admin.site.register(Board)
admin.site.register(Task)
