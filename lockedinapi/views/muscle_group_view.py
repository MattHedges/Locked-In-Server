from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lockedinapi.models import MuscleGroup



class MuscleGroupView(ViewSet):
    """Level up event view"""

    def retrieve(self, request, pk):
        musclegroup = MuscleGroup.objects.get(pk=pk)
        serializer = MusclegroupSerializer(musclegroup)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def list(self, request):
        musclegroup = MuscleGroup.objects.all()
        serializer = MusclegroupSerializer(musclegroup, many=True)
        return Response(serializer.data)

class MusclegroupSerializer(serializers.ModelSerializer):
    """JSON serializer for event
    """
    
    class Meta:
        model = MuscleGroup
        fields = ('id', 'muscle' )
        depth = 1