
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()


        # Create users
        ironman = User.objects.create_user(email='ironman@marvel.com', username='ironman', password='password')
        captain = User.objects.create_user(email='captain@marvel.com', username='captain', password='password')
        batman = User.objects.create_user(email='batman@dc.com', username='batman', password='password')
        superman = User.objects.create_user(email='superman@dc.com', username='superman', password='password')

        # Create teams and assign members by IDs
        marvel = Team.objects.create(name='Marvel', member_ids=[ironman.id, captain.id])
        dc = Team.objects.create(name='DC', member_ids=[batman.id, superman.id])

        # Create activities
        Activity.objects.create(user_id=ironman, type='run', duration=30)
        Activity.objects.create(user_id=captain, type='swim', duration=25)
        Activity.objects.create(user_id=batman, type='cycle', duration=45)
        Activity.objects.create(user_id=superman, type='fly', duration=60)

        # Create workouts and assign suggested_for_ids
        pushups = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for_ids=[ironman.id, batman.id])
        situps = Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for_ids=[captain.id, superman.id])
        flying = Workout.objects.create(name='Flying', description='Fly for 10 minutes', suggested_for_ids=[superman.id])

        # Create leaderboard and assign teams by IDs
        leaderboard = Leaderboard.objects.create(name='Weekly', start_date='2024-01-01', end_date='2024-01-07', team_ids=[marvel.id, dc.id])

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
