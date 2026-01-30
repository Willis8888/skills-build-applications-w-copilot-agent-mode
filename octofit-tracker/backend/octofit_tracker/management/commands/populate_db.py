from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data using Djongo's raw collection interface
        from django.db import connection
        db = connection.cursor().db_conn.client['octofit_db']
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workout.delete_many({})
        db.user.delete_many({})
        db.team.delete_many({})

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel', is_superhero=True)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel', is_superhero=True)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc', is_superhero=True)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team='dc', is_superhero=True)

        # Create activities
        Activity.objects.create(user=tony, type='run', duration=30, points=10, date=timezone.now().date())
        Activity.objects.create(user=steve, type='walk', duration=60, points=8, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='cycle', duration=45, points=12, date=timezone.now().date())
        Activity.objects.create(user=clark, type='swim', duration=50, points=15, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=18, month='January')
        Leaderboard.objects.create(team=dc, points=27, month='January')

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='strength')
        Workout.objects.create(name='Jogging', description='Jog for 30 minutes', suggested_for='endurance')
        Workout.objects.create(name='Yoga', description='30 minutes of yoga', suggested_for='flexibility')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
