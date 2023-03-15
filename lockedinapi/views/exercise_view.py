from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lockedinapi.models import Exercise, Difficulty, MuscleGroup, Equipment
from rest_framework.decorators import action


class ExerciseView(ViewSet):
    """Level up exercise view"""

    def retrieve(self, request, pk):
        exercise = Exercise.objects.get(pk=pk)
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)

    def create(self, request):

        exercise = Exercise.objects.get(user=request.auth.user)
        difficulty = Difficulty.objects.get(pk=request.data["description"])
        muscleGroup = MuscleGroup.objects.get(pk=request.data["muscle"])
        equipment = Equipment.objects.get(pk=request.data["name"])

        exercise = Exercise.objects.create(
        name=request.data["name"],
        description=request.data["description"],
        difficulty=difficulty,
        exercise=exercise,
        muscleGroup = muscleGroup,
        equipment = equipment,
        video = request.data["video"]
        )
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        difficulty = Difficulty.objects.get(pk=request.data["description"])
        muscleGroup = MuscleGroup.objects.get(pk=request.data["muscle"])
        equipment = Equipment.objects.get(pk=request.data["name"])

        exercise = Exercise.objects.get(pk=pk)
        exercise.name = request.data["name"]
        exercise.description = request.data["description"]
        difficulty = difficulty
        muscleGroup = muscleGroup
        equipment = equipment
        exercise.video = request.data["video"]
        exercise.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


    def list(self, request):
        exercise = Exercise.objects.all()
        serializer = ExerciseSerializer(exercise, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk):
        exercise = Exercise.objects.get(pk=pk)
        exercise.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ExerciseSerializer(serializers.ModelSerializer):
    """JSON serializer for exercise
    """
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'description', 'difficulty', 'muscleGroup', 'equipment', 'video' )
        depth = 1