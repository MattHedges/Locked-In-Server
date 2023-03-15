from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lockedinapi.models import Routine, ExerciseRoutine, Exercise
from rest_framework.decorators import action
from django.contrib.auth import get_user_model



class RoutineView(ViewSet):
    """Level up routine view"""

    def retrieve(self, request, pk):
        routine = Routine.objects.get(pk=pk)
        serializer = RoutineSerializer(routine)
        return Response(serializer.data)

    def create(self, request):
        # Get the user instance from the request
        user = get_user_model().objects.get(pk=request.user.pk)

        routine = Routine.objects.create(
            name=request.data["name"],
            user=user
        )
        serializer = RoutineSerializer(routine)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):


        routine = Routine.objects.get(pk=pk)
        routine.name = request.data["name"]
        routine.user = request.auth.user

        exercise_routines_data = request.data.get("exercise_routines", None)
        if exercise_routines_data is not None:
            exercise_routines = []
            for exercise_routine_id in exercise_routines_data:
                exercise_routine = ExerciseRoutine.objects.get(pk=exercise_routine_id)
                exercise_routines.append(exercise_routine)
            routine.exercise_routines.set(exercise_routines)

        routine.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        routine = Routine.objects.all()
        serializer = RoutineSerializer(routine, many=True)
        return Response(serializer.data)


    def destroy(self, request, pk):
        routine = Routine.objects.get(pk=pk)
        routine.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class RoutineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routine
        fields = ('id','name', 'user', 'exerciseRoutine')
        depth = 1