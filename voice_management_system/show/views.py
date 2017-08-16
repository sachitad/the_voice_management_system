from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from rest_framework import filters

from .models import MentorTeam
from .serializers import MentorTeamSerializer, CandidateDetailSerializer
from .permissions import IsAdminOrMentor

User = get_user_model()


class MentorTeamViewSet(viewsets.ReadOnlyModelViewSet):
    """
    GET - /teams/
    search - If passed in will filter with mentor name and team name
    Return list of teams
    If user is Mentor - return teams that he/she is mentoring
    If user is Admin - return all the teams

    GET - /teams/:id/
    Retrieve a single team
    """
    queryset = MentorTeam.objects.all()
    serializer_class = MentorTeamSerializer
    permission_classes = [IsAuthenticated, IsAdminOrMentor]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('team_name', 'mentor__name')

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset
        if user.user_type == 'M':
            queryset = queryset.filter(mentor=user)

        return queryset


class CandidateDetailView(RetrieveAPIView):
    """
    Retrieve single candidate detail and all of his/her activities

    GET - /candidate/:id/
    """
    queryset = User.objects.all()
    serializer_class = CandidateDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminOrMentor]
