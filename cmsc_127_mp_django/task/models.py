from django.db import models

from django.conf import settings

class Card(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cards', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=8060, blank=True, null=True)
    image = models.CharField(max_length=320)
    is_marked = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False)
    is_history = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('date_added',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.user.slug}/{self.slug}/'

class Board(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='boards', on_delete=models.CASCADE)
    card = models.ForeignKey(Card, related_name='boards', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=8060, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.user.slug}/{self.card.slug}/{self.slug}/'

class Task(models.Model):

    TODO = 'todo'
    DONE = 'done'

    STATUS_CHOICES = (
        (TODO, 'Todo'),
        (DONE, 'Done')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks', on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=8060, blank=True, null=True)
    is_marked = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO)
    date_added = models.DateField(auto_now_add=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.user.slug}/{self.board.card.slug}/{self.board.slug}/{self.slug}/'