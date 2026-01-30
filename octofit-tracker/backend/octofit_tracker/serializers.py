from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'team', 'is_superhero']
    def get_id(self, obj):
        return str(obj.id)

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'description']
    def get_id(self, obj):
        return str(obj.id)

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'type', 'duration', 'points', 'date']
    def get_id(self, obj):
        return str(obj.id)

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'points', 'month']
    def get_id(self, obj):
        return str(obj.id)

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for']
    def get_id(self, obj):
        return str(obj.id)
