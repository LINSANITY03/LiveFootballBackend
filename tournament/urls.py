from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "tournament"

# urlpatterns = [
#     path('', views.TournamentListView.as_view(), name="tournament_list")

# ]

router = DefaultRouter()
router.register(r'', views.TournamentView, basename='tournament_list')
urlpatterns = router.urls
