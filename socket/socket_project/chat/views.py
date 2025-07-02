from django.shortcuts import render
from .models import ChatMessage

def index(request):
    return render(request, "chat/index.html", {})

def room(request, room_name):
    messages = ChatMessage.objects.filter(room_name=room_name).order_by('timestamp')
    print("=====================")
    print(room_name)
    print(messages)
    print("=====================")
    context = {
        "room_name": room_name,
        "messages": messages,
    }
    return render(request, "chat/room.html", context)