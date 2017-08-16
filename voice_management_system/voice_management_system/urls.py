from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from show import views


router = DefaultRouter()
router.register(r'teams', views.MentorTeamViewSet)

urlpatterns = [
    url(r'api/v1/', include(router.urls)),
    url(r'^api/v1/candidate/(?P<pk>\d+)/$', views.CandidateDetailView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/v1/', include('rest_auth.urls'))
]
