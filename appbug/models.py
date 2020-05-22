from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username


class Bug(models.Model):
    NEW = 'N'
    IN_PROGRESS = 'P'
    DONE = 'D'
    INVALID = 'I'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid'),
    ]

    title = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    author = models.ForeignKey(
        CustomUser, related_name='%(class)s_author', null=True,
        blank=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(
        CustomUser, related_name='%(class)s_owner', null=True,
        blank=True, on_delete=models.SET_NULL)
    closer = models.ForeignKey(
        CustomUser, related_name='%(class)s_closer', null=True,
        blank=True, on_delete=models.SET_NULL)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=NEW,
    )

    def __str__(self):
        return self.title
