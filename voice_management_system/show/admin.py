from django.contrib import admin

from .models import Activity, MentorScore, MentorTeam


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass


@admin.register(MentorTeam)
class MentorTeamAdmin(admin.ModelAdmin):
    pass


@admin.register(MentorScore)
class MentorScoreAdmin(admin.ModelAdmin):
    pass
