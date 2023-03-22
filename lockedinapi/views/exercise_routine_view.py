from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lockedinapi.models import Exercise, Routine, ExerciseRoutine



class ExerciseRoutineView(ViewSet):
    
    def create(self, request):

        exercise = Exercise.objects.get(pk=request.data["exercise"])
        routine = Routine.objects.get(pk=request.data["routine"])

        exerciseRoutine = ExerciseRoutine.objects.create(
                exercise = exercise,
                routine = routine
                )
        serializer = ExerciseRoutineSerializer(exerciseRoutine)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        exerciseroutine = ExerciseRoutine.objects.get(pk=pk)
        serializer = ExerciseRoutineSerializer(exerciseroutine)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def list(self, request):
        exerciseroutine = ExerciseRoutine.objects.all()
        serializer = ExerciseRoutineSerializer(exerciseroutine, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        exerciseRoutine = ExerciseRoutine.objects.get(pk=pk)
        exerciseRoutine.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        routine = Routine.objects.get(pk=request.data["routine"])
        exercise = Exercise.objects.get(pk=request.data["exercise"])

        exerciseRoutine = ExerciseRoutine.objects.get(pk=pk)
        exerciseRoutine.routine = routine
        exerciseRoutine.exercise = exercise

        exerciseRoutine.save()

        return Response( status=status.HTTP_204_NO_CONTENT)
    
class ExerciseRoutineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExerciseRoutine
        fields = ('id', 'exercise', 'routine' )
