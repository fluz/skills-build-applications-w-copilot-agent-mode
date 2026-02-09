

from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    member_ids = models.ArrayReferenceField(
        to=User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

class Activity(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()  # in minutes
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id.username} - {self.type}"

class Leaderboard(models.Model):
    name = models.CharField(max_length=100)
    team_ids = models.ArrayReferenceField(
        to=Team,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for_ids = models.ArrayReferenceField(
        to=User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
