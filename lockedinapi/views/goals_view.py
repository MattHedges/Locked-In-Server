from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lockedinapi.models import Goal, Exercise
from rest_framework.decorators import action
from django.contrib.auth.models import User



class GoalView(ViewSet):
    """Level up goal view"""

    def retrieve(self, request, pk):
        goal = Goal.objects.get(pk=pk)
        serializer = GoalSerializer(goal)
        return Response(serializer.data)

    def create(self, request):

        goal = Goal.objects.create(
            currentWeight= request.data["currentWeight"],
            goalWeight=request.data["goalWeight"],
            user=request.auth.user,
            timeframe = request.data["timeframe"]
            )
        serializer = GoalSerializer(goal)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):

        user = User.objects.get(id=request.data["user"])

        goal = Goal.objects.get(pk=pk)
        goal.currentWeight = request.data["currentWeight"]
        goal.goalWeight = request.data["goalWeight"]
        goal.user = user
        goal.timeframe = request.data["timeframe"]

        goal.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


    def list(self, request):
        if "user" in request.query_params:
            goal = Goal.objects.filter(user_id=request.query_params['user'])
        else: 
            goal = Goal.objects.all()
        serializer = GoalSerializer(goal, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk):
        goal = Goal.objects.get(pk=pk)
        goal.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    # add a completed goals section that can retrieve all of a users previous goals

class GoalSerializer(serializers.ModelSerializer):
    """JSON serializer for goal
    """
    class Meta:
        model = Goal
        fields = ('id', 'currentWeight', 'goalWeight', 'user', 'timeframe' )