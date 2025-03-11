from django.urls import path
from .views import PollListCreateView, VoteCreateView, PollResultsView

urlpatterns = [
    path('polls/', PollListCreateView.as_view(), name='polls'),
    path('polls/<int:poll_id>/vote/', VoteCreateView.as_view(), name='vote'),
    path('polls/<int:poll_id>/results/', PollResultsView.as_view(), name='results'),
]
