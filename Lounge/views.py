from rest_framework.response import Response
from Lounge.models import AirpotLoungeModel
from rest_framework import generics, status
from Lounge.serializers import LoungeSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import permissions

@api_view(['DELETE',])
def delete_all(request):
    """
    :param request:  Delete all Lounge data
    :return: None
    """
    permission_classes = (IsAuthenticated,)
    if request.method.lower() != "delete":
        response = {"Result": "False", "Message": "METHOD NOT FOUND"}
        return Response(response)
    AirpotLoungeModel.objects.all().delete()
    response = {"Result": "Success", "Delete": True}
    return Response(response)

class LoungeListView(generics.ListAPIView):
    """
    params : list all data from the Lounge list
    """
    queryset = AirpotLoungeModel.objects.all()  # .filter(status='active')
    serializer_class = LoungeSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

class LoungeView(APIView):
    """
    params : name , price, size
    """
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk, format=None):
        lounge = self.get_object(pk)
        if isinstance(lounge, str):
            return Response({"Result": False, "Data": "NOT_FOUND"}, status=status.HTTP_201_CREATED)
        serializer = LoungeSerializer(lounge, data=request.data)

        if serializer.is_valid():
            serializer.save()
            default_response = {"Result": "Success", "data": serializer.data}
            return Response(default_response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        file_serializer = LoungeSerializer(data=request.data, context={'request': request})
        if file_serializer.is_valid():
            file_serializer.save()
            name = file_serializer.data.get("name")
            created_at = file_serializer.data.get("created_at")
            default_data = {"Result": "Passed", "Name": name, "Created_At": created_at}
            return Response(default_data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        if isinstance(event, str):
            default_data = {"Result": "NOT_FOUND"}
            return Response(default_data, status=status.HTTP_204_NO_CONTENT)
        event.delete()
        default_data = {"Result": "Passed"}
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        try:
            return AirpotLoungeModel.objects.get(pk=pk)
        except AirpotLoungeModel.DoesNotExist:
            return 'NOT_FOUND'
