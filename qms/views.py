from django.http import HttpResponse
from rest_framework import viewsets
from .serializer import QueueUserSerializer, QueueItemSerializer
from .models import QueueUser, QueueItem
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world! This is the index page of the queue app.")

def admin(request):
    return render(request, 'admin.html')

class QueueUserViewSet(viewsets.ModelViewSet):
    queryset = QueueUser.objects.all()
    serializer_class = QueueUserSerializer

def queue_users(request):
    users = QueueUser.objects.all()
    items = QueueItem.objects.all()
    return render(request, 'index.html', {'users': users, 'items': items})

class QueueItemViewSet(viewsets.ModelViewSet):
    queryset = QueueItem.objects.all()
    serializer_class = QueueItemSerializer



# class QueueUserView:
#         users = QueueUser.objects.all()
#         serializer = QueueUserSerializer(users, many=True)
#         return HttpResponse(serializer.data)
    
# class QueueItemView:
#     def get(self, request):
#         items = QueueItem.objects.all()
#         serializer = QueueItemSerializer(items, many=True)
#         return HttpResponse(serializer.data)
    
#     def post(self, request):
#         serializer = QueueItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return HttpResponse(serializer.data, status=201)
#         return HttpResponse(serializer.errors, status=400)
