from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from django.contrib.auth.models import User

class UserView(ViewSet):
    """Level up goal view"""

    def retrieve(self, request, pk):
        goal = Goal.objects.get(pk=pk)
        serializer = GoalSerializer(goal)
        return Response(serializer.data)

    def create(self, request):

        user = User.objects.create(
            currentWeight= request.data["currentWeight"],
            goalWeight=request.data["goalWeight"],
            user=request.auth.user,
            timeframe = request.data["timeframe"]
            )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)