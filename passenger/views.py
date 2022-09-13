from django.shortcuts import render

# Create your views here.

@api_view(['GET','POST'])
def passenger_list(request):

    if request.method == 'GET':
        passengers = Passenger.objects.all():
        serializer = PassengerSerializer(passengers, many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        serializer = PassengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
