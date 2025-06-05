from django.urls import path
from . import views

# If you want to change the URL of polls detail view to something like
# /polls/speficis/12/, instead of in the templates you change it here.
# ex: path("specifics/<int:question_id>/", views.detail, name="detail")

# The app_name is used to namespace the URLs in this app.
app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]