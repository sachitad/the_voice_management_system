from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import ValidationError


class User(AbstractUser):
    # Candidate user type don't have any major role in the system yet ..
    # but this might change in the future
    USER_TYPES = (
        ('C', _('Candidate')),
        ('M', _('Mentor')),
        ('A', _('Admin')),
    )
    user_type = models.CharField(_('Type of User'), max_length=1,
                                 choices=USER_TYPES)
    # First Name and Last Name do not cover name patterns around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    team = models.ForeignKey('show.MentorTeam', related_name='candidates',
                             blank=True, null=True)

    def clean_fields(self, exclude=None):
        super(User, self).clean_fields(exclude=exclude)
        # If user is candidate make team mandatory
        if self.user_type == 'C' and self.team is None:
            raise ValidationError(
                {'team': _('Candidate must be assigned to a team')}
            )

    def __str__(self):
        return self.name or self.username

    def average_score(self):
        """
        Get the average score of user calculated from all of his activities
        :return: score (int) or None
        """
        if self.user_type == 'C':   # only if user is candidate
            activities = self.activities.all()
            # If someone hasn't participate in any activity return None
            if activities:
                total_activities = activities.count()
                total_score = 0
                for activity in activities:
                    total_score += activity.average_score()
                # Convert to the nearest int
                return round(total_score / total_activities)
        return
