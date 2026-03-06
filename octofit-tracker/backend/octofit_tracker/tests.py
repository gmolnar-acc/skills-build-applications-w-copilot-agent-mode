from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass')
        self.assertEqual(user.email, 'spiderman@marvel.com')

    def test_team_creation(self):
        team = Team.objects.create(name='Avengers')
        self.assertEqual(team.name, 'Avengers')

    def test_activity_creation(self):
        activity = Activity.objects.create(name='Jump', user='spiderman', team='Avengers')
        self.assertEqual(activity.name, 'Jump')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='Avengers', points=200)
        self.assertEqual(leaderboard.team, 'Avengers')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Squats', description='Do 30 squats')
        self.assertEqual(workout.name, 'Squats')
