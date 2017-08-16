import random

from django.contrib.auth import get_user_model
from django.utils import timezone

import factory

from show.models import MentorTeam, Activity, MentorScore

User = get_user_model()


class MentorFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    name = 'PSY'

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.Sequence(lambda n: 'user%d@gmail.com' % n)
    password = factory.PostGenerationMethodCall('set_password', 'valid')

    is_superuser = False
    is_staff = False
    is_active = True
    user_type = 'M'


class AdminFactory(MentorFactory):
    user_type = 'A'
    username = factory.Sequence(lambda n: 'admin%d' % n)


class MentorTeamFactory(factory.DjangoModelFactory):
    class Meta:
        model = MentorTeam

    team_name = 'Team 1'
    mentor = factory.SubFactory(MentorFactory)


class CandidateFactory(MentorFactory):
    user_type = 'C'
    team = factory.SubFactory(MentorTeamFactory)


class ActivityFactory(factory.DjangoModelFactory):
    song_name = 'Let it be'
    date_of_performance = timezone.now().date()
    candidate = factory.SubFactory(CandidateFactory)

    class Meta:
        model = Activity


class MentorScoreFactory(factory.DjangoModelFactory):
    activity = factory.SubFactory(ActivityFactory)
    mentor = factory.SubFactory(MentorFactory)
    score = 80

    class Meta:
        model = MentorScore


def create_data():
    """
    Instead of just calling factories.. effort have been put up
    to create individual ones for the proper data to test with
    - First create mentors
    - Then admins
    - Create 4 different teams - each team for individual mentor
    - Create about 25 candidates and assign them in the created team
      (4-6 in each team)
    - Create activities for each candidate and assign score to each
      activities by all the mentors
    """
    # Create super admin first
    User.objects.create_superuser(username='admin', email='admin@admin.com',
                                  password='superman')

    mentor1 = MentorFactory()
    mentor2 = MentorFactory(name='Shakira')
    mentor3 = MentorFactory(name='Justin Bieber')
    mentor4 = MentorFactory(name='Katie Perry')

    for i in range(4):
        AdminFactory(name='John Admin' + str(i))

    team_name = lambda mentor_name: 'Team {}'.format(mentor_name)
    team1 = MentorTeamFactory(team_name=team_name(mentor1.name),
                              mentor=mentor1)
    team2 = MentorTeamFactory(team_name=team_name(mentor2.name),
                              mentor=mentor2)
    team3 = MentorTeamFactory(team_name=team_name(mentor3.name),
                              mentor=mentor3)
    team4 = MentorTeamFactory(team_name=team_name(mentor4.name),
                              mentor=mentor4)

    mentors = [mentor1, mentor2, mentor3, mentor4]
    score = lambda activity: [
        MentorScoreFactory(activity=activity, mentor=i,
                           score=random.randint(0, 100)) for i in
        mentors]

    for i in range(0, 20):
        # create random candidates with 4/5 candidates in each team
        # Then create activity for them and scores by each mentor
        if i < 5:
            c1 = CandidateFactory(team=team1, name='candidate' + str(i))
            for x in range(0, 5):
                score(ActivityFactory(candidate=c1,
                                      song_name='Song' + str(x)))
        elif 5 <= i <= 10:
            c2 = CandidateFactory(team=team2, name='candidate' + str(i))
            for x in range(0, 5):
                score(ActivityFactory(candidate=c2,
                                      song_name='Song' + str(x)))
        elif 10 <= i <= 15:
            c3 = CandidateFactory(team=team3, name='candidate' + str(i))
            for x in range(0, 5):
                score(ActivityFactory(candidate=c3,
                                      song_name='Song' + str(x)))
        elif 15 <= i <= 20:
            c4 = CandidateFactory(team=team4, name='candidate' + str(i))
            for x in range(0, 5):
                score(ActivityFactory(candidate=c4,
                                      song_name='Song' + str(x)))
