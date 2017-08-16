from rest_framework import serializers

from .models import MentorTeam, Activity, MentorScore
from users.models import User


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name',)


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'name',)


class MentorTeamSerializer(serializers.ModelSerializer):
    candidates = CandidateSerializer(many=True)

    class Meta:
        model = MentorTeam
        fields = ('pk', 'team_name', 'candidates', 'team_average_score')


class MentorScoreSerializer(serializers.ModelSerializer):
    mentor = serializers.CharField(source='mentor.name', read_only=True)

    class Meta:
        model = MentorScore
        fields = ('mentor', 'score')


class ActivitySerializer(serializers.ModelSerializer):
    scores = MentorScoreSerializer(many=True)

    class Meta:
        model = Activity
        fields = ('song_name', 'date_of_performance', 'scores',)


class CandidateDetailSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True)
    team_average_score = serializers.SerializerMethodField()

    def get_team_average_score(self, obj):
        return obj.team.team_average_score()

    class Meta:
        model = User
        fields = ('pk', 'name', 'activities', 'average_score',
                  'team_average_score')


