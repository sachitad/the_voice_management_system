from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Sum


User = get_user_model()


class MentorTeam(models.Model):
    """
    This model stores the team information
    - One team will have a name, one mentor and multiple candidates.
    - One mentor can act as a mentor to multiple teams
    - One candidate on the other hand will belong to only one team
    """
    team_name = models.CharField(_('Name of Team'), max_length=250)
    mentor = models.ForeignKey(User, limit_choices_to={'user_type': 'M'},
                               related_name='team_mentor')

    def __str__(self):
        return '{}: team by {}'.format(self.team_name, self.pk)

    def team_average_score(self):
        """
        Get the average score of all the candidates in the team
        and from that get the average score of the team
        """
        total_score = 0
        # Some team might be in the candidate selection process
        if self.candidates.all():
            for candidate in self.candidates.all():
                # Some team member might not have any activity just yet
                if candidate.average_score():
                    average_score = candidate.average_score()
                    total_score += average_score
            return round(total_score/self.candidates.count())
        return


class Activity(models.Model):
    """
    Model to store candidate activities (i.e the song they performed)
    """
    song_name = models.CharField(max_length=255)
    date_of_performance = models.DateField()
    candidate = models.ForeignKey(User, limit_choices_to={'user_type': 'C'},
                                  related_name='activities')

    def average_score(self):
        """
        Get the average score of this activity
        """
        scores = self.scores.all().aggregate(Sum('score'))['score__sum']
        # Instead of showing in float round off to nearest int
        return round(scores/3)

    def __str__(self):
        return '{} performed by {}'.format(self.song_name, self.candidate)

    class Meta:
        verbose_name_plural = _('Activities')


class MentorScore(models.Model):
    """
    All mentors are able to vote on activity of every contestant. This model
    facilitates that
    """
    activity = models.ForeignKey(Activity, related_name='scores')
    mentor = models.ForeignKey(User, limit_choices_to={'user_type': 'M'},
                               related_name='scores')
    score = models.IntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
    ])

    class Meta:
        """
        One mentor can cast score in a activity only once
        """
        unique_together = ('activity', 'mentor')

    def __str__(self):
        return '{} - Score by {}: {}'.format(self.activity, self.mentor,
                                             self.score)
