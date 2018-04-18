#from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt
#from django.http import JsonResponse
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer



class MessageViewSet(viewsets.ModelViewSet):
	queryset = Message.objects.all().order_by('-created_at')
	serializer_class = MessageSerializer



#def index(request):
 #   return render(request, 'webapp/index.html', {})

#@csrf_exempt
#def test_api(request):
 #   return JsonResponse({'foo': 'bar'})
