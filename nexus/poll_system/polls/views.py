from rest_framework import generics
from .models import Poll, Option, Vote
from .serializers import PollSerializer, VoteSerializer

class PollListCreateView(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class VoteCreateView(generics.CreateAPIView):
    serializer_class = VoteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PollResultsView(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
