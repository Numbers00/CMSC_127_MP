from django.db import models

from django.contrib.auth.models import AbstractUser

from django.core.exceptions import ValidationError

from task.models import Card, Board, Task

# Create your models here.
class User(AbstractUser):
    BRONZE = 'bronze'
    SILVER = 'silver'
    GOLD = 'gold'

    STATUS_CHOICES = (
        (BRONZE, 'Bronze'),
        (SILVER, 'Silver'),
        (GOLD, 'Gold')
    )

    username = models.CharField(max_length=32, unique=True, null=False, blank=False)
    email = models.CharField(max_length=128, unique=True, null=False, blank=False)
    bio = models.CharField(max_length=1280, null=True, blank=True, default="")
    quote = models.CharField(max_length=128, null=True, blank=True, default="")
    profile_picture = models.CharField(max_length=255, null=True, blank=True, default="https://s.gr-assets.com/assets/nophoto/user/u_200x266-e183445fd1a1b5cc7075bb1cf7043306.png")
    bg_image = models.CharField(max_length=255, null=True, blank=True, default="")
    plan_level = models.CharField(max_length=10, choices=STATUS_CHOICES, default=BRONZE)
    password = models.CharField(max_length=128, null=False, blank=False)
    is_visible = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    REQUIRED_FIELDS = ["email", "bio", "quote", "profile_picture", "bg_image", "plan_level", "is_visible", "slug"]

    class Meta:
        ordering = ('date_joined',)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return f'/{self.slug}/'