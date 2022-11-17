from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from social.models import Room

from .serializers import ChatSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api '
        'GET /api/rooms '
        'GET /api/rooms/:id '
        'POST /api/addroom'
    ] 
    return Response(routes)

@api_view(['GET'])
def apiRooms(request):
    rooms = Room.objects.all()
    serializer = ChatSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def specificRoom(request, pk):
    rooms = Room.objects.get(id=pk)
    serializer = ChatSerializer(rooms, many=False)
    return Response(serializer.data)

# @api_view(['POST'])
# def addRoom(request):
#     serializer = ChatSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

class RoomAPIView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = ChatSerializer
