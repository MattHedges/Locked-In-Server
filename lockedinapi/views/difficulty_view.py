from lockedinapi.models import Difficulty
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

class DifficultyView(ViewSet):

    def retrieve(self, request, pk):
        difficulty = Difficulty.objects.get(pk=pk)
        serializer = DifficultySerializer(difficulty)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def list(self, request):
        difficulty = Difficulty.objects.all()
        serializer = DifficultySerializer(difficulty, many=True)
        return Response(serializer.data)

class DifficultySerializer(serializers.ModelSerializer):
    """JSON serializer for event
    """
    
    class Meta:
        model = Difficulty
        fields = ('id', 'description' )
        depth = 1