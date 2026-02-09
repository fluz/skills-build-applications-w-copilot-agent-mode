
from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # Teams are many-to-many
    # Workouts are many-to-many (suggested_for)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User, related_name='teams')

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()  # in minutes
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.type}"

class Leaderboard(models.Model):
    name = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team, related_name='leaderboards')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField(User, related_name='workouts', blank=True)

    def __str__(self):
        return self.name
