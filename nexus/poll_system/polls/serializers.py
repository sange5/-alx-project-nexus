from rest_framework import serializers
from .models import Poll, Option, Vote

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'poll']

class PollSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, required=False)  

    class Meta:
        model = Poll
        fields = ['id', 'title', 'created_at', 'expiry_date', 'options']

    def create(self, validated_data):
        options_data = validated_data.pop('options', [])  
        poll = Poll.objects.create(**validated_data)  

        for option_data in options_data:
            Option.objects.create(poll=poll, **option_data)  
        return poll

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'user', 'option']

    def validate(self, data):
        """Ensure a user can only vote once per poll."""
        user = data.get('user')
        option = data.get('option')

        if Vote.objects.filter(user=user, option__poll=option.poll).exists():
            raise serializers.ValidationError("You have already voted for this poll.")

        return data
