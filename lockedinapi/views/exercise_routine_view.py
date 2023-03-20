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
    
    def destroy(self, request, pk):
        exerciseRoutine = ExerciseRoutine.objects.get(pk=pk)
        exerciseRoutine.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ExerciseRoutineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExerciseRoutine
        fields = ('id', 'exercise', 'routine' )
        depth = 1